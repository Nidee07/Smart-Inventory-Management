from django.urls import path
from . import views

urlpatterns = [
    path('inventory/<str:sku>/', views.get_inventory),
    path('reorder/', views.trigger_reorder),
]
