from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import AddProduct
from .models import Product,Cart, CartItem
from django.db.models import Sum, F
# Create your views here.
def home(request):
    products=Product.objects.all()
    print(products)
    context={
        'products':products
    }
    
    return render(request,'main/home.html',context)


def add_product(request):
    if request.method=="POST":
        form=AddProduct(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            form.save()  
            return redirect("home")
    
    form=AddProduct()
    context={
        'form':form
    }
    return render(request,'main/addProduct.html',context)

def product_details(request,id):
    product=Product.objects.get(id=id)
    print(product)
    return render(request,'main/product_details.html',{'product':product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get or create the cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        # If the item already exists, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')  # Redirect to the cart view

@login_required
def view_cart(request):
    cart,created = Cart.objects.get_or_create(user=request.user)
    # items = cart.items.all()  # Fetch all items in the cart
    items = cart.items.select_related('product').annotate(
    item_total=F('quantity') * F('product__price')
)
    total_price = items.aggregate(total=Sum('item_total'))['total'] or 0
    print(items.values())
    # total_price = cart.total_price()  # Calculate total price
    return render(request, 'main/view_cart.html', {'items': items,'total_price':total_price})