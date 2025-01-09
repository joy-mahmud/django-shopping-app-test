from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addProduct/',views.add_product, name="add_product"),
    path('edit-product/<int:product_id>/', views.update_product, name='update_product'),
      path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
]
