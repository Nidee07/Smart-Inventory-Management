from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Inventory, Product, Supplier, ReorderRequest
from django.utils.timezone import now
import requests

@api_view(['GET'])
def get_inventory(request, sku):
    try:
        product = Product.objects.get(sku=sku)
        inventory = Inventory.objects.filter(product=product)
        data = [{"warehouse": inv.warehouse.name, "quantity": inv.quantity} for inv in inventory]
        return Response({"product": product.name, "inventory": data})
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

@api_view(['POST'])
def trigger_reorder(request):
    sku = request.data.get('sku')
    quantity = int(request.data.get('quantity', 0))
    try:
        product = Product.objects.get(sku=sku)
        supplier = Supplier.objects.first()  # Update as needed for logic
        reorder = ReorderRequest.objects.create(product=product, supplier=supplier, quantity=quantity)

        # Call supplier API
        payload = {"product_sku": sku, "quantity": quantity}
        headers = {"Authorization": f"Bearer {supplier.api_key}"}
        response = requests.post(supplier.api_endpoint, json=payload, headers=headers)

        reorder.status = 'Ordered' if response.status_code == 200 else 'Failed'
        reorder.save()

        return Response({"status": reorder.status})
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
