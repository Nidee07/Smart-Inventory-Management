import time
import random
import requests

API_ENDPOINT = "http://localhost:8000/inventory/"
SKU_LIST = ["ITEM001", "ITEM002"]

def simulate_inventory_update():
    while True:
        sku = random.choice(SKU_LIST)
        new_qty = random.randint(10, 150)
        data = {'sku': sku, 'quantity': new_qty}
        print(f"Updating {sku} to {new_qty}")
        try:
            resp = requests.post(f"{API_ENDPOINT}{sku}/", json=data)
            print(resp.status_code, resp.text)
        except Exception as e:
            print(e)
        time.sleep(5)  # Simulate sensor update interval

if __name__ == "__main__":
    simulate_inventory_update()
