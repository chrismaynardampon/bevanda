from datetime import date

from django.contrib import messages
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now

from .forms import InventoryForm, PreparationInventoryForm, ProductForm
from .models import EventBooking, Inventory, PreparationInventory, Product


#home view
def home(request):
    total_events = EventBooking.objects.count()
    total_inventory = Inventory.objects.count()
    today = now().date()
    events_today = EventBooking.objects.filter(event_date=today).count()

    context = {
        'total_events': total_events,
        'total_inventory': total_inventory,
        'events_today': events_today,
    }

    return render(request, 'home.html', context)


# Index view
def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        inventory = Inventory.objects.filter(
            product_name__icontains=search_query) | Inventory.objects.filter(
            category__icontains=search_query)
    else:
        inventory = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventory': inventory, 'search_query': search_query})

# Add inventory item
def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item added successfully!")
            return redirect('index')
    else:
        form = InventoryForm()
    return render(request, 'add_inventory.html', {'form': form})

# Edit inventory item
def edit_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item updated successfully!")
            return redirect('index')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'edit_inventory.html', {'item': item, 'form': form})

# Delete inventory item
def delete_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    item.delete()
    messages.success(request, "Inventory item deleted successfully!")
    return redirect('index')

# Transfer inventory item
def transfer_item(request, id):
    item = get_object_or_404(Inventory, id=id)
    if request.method == 'POST':
        transfer_quantity = int(request.POST['transfer_quantity'])
        if transfer_quantity > item.quantity:
            messages.error(request, "Transfer quantity exceeds available quantity.")
        else:
            # Deduct from Inventory
            item.quantity -= transfer_quantity
            item.save()

            # Add to PreparationInventory
            new_transfer = PreparationInventory(
                product_name=item.product_name,
                quantity=transfer_quantity,
                transfer_date=date.today().strftime("%Y-%m-%d")
            )
            new_transfer.save()

            messages.success(request, f"Transferred {transfer_quantity} units of {item.product_name}.")
        return redirect('index')
    return render(request, 'transfer_item.html', {'item': item})

# Preparation inventory
def preparation_inventory(request):
    transfers = PreparationInventory.objects.all()
    return render(request, 'preparation_inventory.html', {'transfers': transfers})

# Update preparation inventory
def update_preparation_inventory(request, id):
    item = get_object_or_404(PreparationInventory, id=id)
    if request.method == 'POST':
        form = PreparationInventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Preparation inventory item updated successfully!")
            return redirect('preparation_inventory')
    else:
        form = PreparationInventoryForm(instance=item)
    return render(request, 'update_preparation_inventory.html', {'item':item, 'form': form})

# Delete preparation inventory item
def delete_preparation_inventory(request, id):
    item = get_object_or_404(PreparationInventory, id=id)
    item.delete()
    messages.success(request, "Preparation inventory item deleted successfully!")
    return redirect('preparation_inventory')

# Generate report
from django.http import HttpResponse
from reportlab.pdfgen import canvas


def download_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="inventory_report.pdf"'

    pdf = canvas.Canvas(response)

    title = "Inventory Report"
    separator = "=" * len(title)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(100, 800, title)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 780, separator)

    y = 750
    line_height = 20

    products = Inventory.objects.all()
    for product in products:
        pdf.drawString(
            100, y,
            f"ID: {product.id} | Name: {product.product_name} | "
            f"Category: {product.category} | Stock: {product.stock} | Quantity: {product.quantity} | Event Date: {product.event_date}"
        )
        y -= line_height

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 750

    pdf.save()
    return response

def download_report2(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="ingredients_report.pdf"'

    pdf = canvas.Canvas(response)

    title = "Ingredients Report"
    separator = "=" * len(title)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(100, 800, title)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 780, separator)

    y = 750
    line_height = 20

    products = Product.objects.all()
    for product in products:
        pdf.drawString(
            100, y,
            f"ID: {product.id} | Name: {product.product_name} | "
            f"Ingredient Type: {product.ingredient_type} | Quantity: {product.quantity}"
        )
        y -= line_height

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 750

    pdf.save()
    return response

#Ingredient List

def product_index(request):
    search_query = request.GET.get('search', '').strip()
    if search_query:
        products = Product.objects.filter(
            models.Q(product_name__icontains=search_query) |
            models.Q(ingredient_type__icontains=search_query)
        )
    else:
        products = Product.objects.all()
    return render(request, 'product_index.html', {'products': products, 'search_query': search_query})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('products')
    
def stock_in(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = request.POST.get('quantity')
    if request.method == 'POST':
        product.quantity += int(quantity)
        product.stock_in_date = now().date()
        product.save()
        
        messages.success(request, f'Successfully added {quantity} units of {product.product_name}.')
        return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'stock_in.html', {'form': form, 'product': product})


def stock_out(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = request.POST.get('quantity')
    if request.method == 'POST':
        product.quantity -= int(quantity)
        product.stock_in_date = now().date()
        product.save()
        
        messages.success(request, f'{quantity} units of {product.product_name} stocked out successfully.')
        return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'stock_out.html', {'form': form, 'product': product})

#Event Booking
def book_event(request):
    if request.method == "POST":
        event_date = request.POST.get("event_date")
        event_time = request.POST.get("event_time")

        # Save the booking
        booking = EventBooking(event_date=event_date, event_time=event_time)
        booking.save()
        messages.success(request, "Event booked successfully!")
        return redirect('book_event')

    # Fetch all booked events
    events = EventBooking.objects.all()
    return render(request, 'event_booking.html', {'events': events})


# Update
def update_event(request, id):
    event = get_object_or_404(EventBooking, id=id)
    if request.method == "POST":
        event.event_date = request.POST.get("event_date")
        event.event_time = request.POST.get("event_time")
        event.save()
        messages.success(request, "Event updated successfully!")
        return redirect('book_event')
    
    return render(request, 'update_event.html', {'event': event})


# Delete
def delete_event(request, id):
    event = get_object_or_404(EventBooking, id=id)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect('book_event')