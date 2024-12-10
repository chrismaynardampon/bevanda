from django import forms

from .models import Inventory, PreparationInventory, Product


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name', 'category', 'stock', 'quantity', 'event_date']

class PreparationInventoryForm(forms.ModelForm):
    class Meta:
        model = PreparationInventory
        fields = ['product_name', 'quantity', 'transfer_date']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'ingredient_type', 'quantity', 'stock_in_date']
        widgets = {
            'stock_in_date': forms.DateInput(attrs={'type': 'date'}),
        }
