from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.index, name='index'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/edit/<int:id>/', views.edit_inventory, name='edit_inventory'),
    path('inventory/delete/<int:id>/', views.delete_inventory, name='delete_inventory'),
    path('inventory/transfer/<int:id>/', views.transfer_item, name='transfer_item'),
    path('preparation_inventory/', views.preparation_inventory, name='preparation_inventory'),
    path('preparation_inventory/update/<int:id>/', views.update_preparation_inventory, name='update_preparation_inventory'),
    path('preparation_inventory/delete/<int:id>/', views.delete_preparation_inventory, name='delete_preparation_inventory'),
    path('inventory/download_report/', views.download_report, name='download_report'),
    path('products/', views.product_index, name='products'),
    path('products/create_product/', views.create_product, name='create_product'),
    path('products/update_product/<int:id>/', views.update_product, name='update_product'),
    path('products/delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('products/stock-in/<int:id>/', views.stock_in, name='stock_in'),
    path('products/stock-out/<int:id>/', views.stock_out, name='stock_out'),
    path('products/download_report/', views.download_report2, name='download_report2'),
    path('book-event/', views.book_event, name='book_event'),
    path('book-event/update/<int:id>/', views.update_event, name='update_event'),
    path('book-event/delete/<int:id>/', views.delete_event, name='delete_event'),
]
