from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models import Product
from .forms import AddProduct,UpdateProduct

# Create your views here.
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    products= Product.objects.all()
    return render(request,'admin/dashboard.html',{'products':products})

@login_required
@user_passes_test(is_admin)
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
    return render(request,'admin/addProduct.html',context)


@login_required
@user_passes_test(is_admin)
def update_product(request,product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            form = UpdateProduct(request.POST, request.FILES, instance=product)
            if form.is_valid():
                print(form)
                form.save()
                return redirect('dashboard')  # Redirect to a product list or detail view
        else:
            form = UpdateProduct(instance=product)
        return render(request, 'admin/edit_product.html', {'form': form,'product':product})