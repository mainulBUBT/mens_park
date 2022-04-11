from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Products

from .forms import ProductForm


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')      
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.success(request, 'User not found!', extra_tags='danger')
            return HttpResponseRedirect(reverse('App_Admin:login'))

        login(request, user)
        return HttpResponseRedirect(reverse('App_Admin:dashboard'))

    return render(request, 'App_Admin/login.html', context={})

@login_required
def admin_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!', extra_tags='danger')
    return HttpResponseRedirect(reverse('App_Admin:login'))


@login_required
def dashboard(request):
    return render(request, 'App_Admin/dashboard.html')

@login_required
def add_products(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Added successfully!', extra_tags='success')
            return HttpResponseRedirect(reverse('App_Admin:add_products'))

    return render(request, 'App_Admin/add_products.html', context={'form':form})

@login_required
def all_products(request):
    products = Products.objects.all()
    return render(request, 'App_Admin/all_products.html', context={'items': products})

@login_required
def edit_product(request,product_id):
    product = Products.objects.get(id=product_id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated successfully!', extra_tags='success')
            return HttpResponseRedirect(reverse('App_Admin:all_products'))
    return render(request, 'App_Admin/edit_product.html', context={'form':form})
    
@login_required
def delete_product(request,product_id):
    product = Products.objects.get(id=product_id).delete()
    messages.success(request, 'Product Deleted successfully!', extra_tags='success')
    return HttpResponseRedirect(reverse('App_Admin:all_products'))