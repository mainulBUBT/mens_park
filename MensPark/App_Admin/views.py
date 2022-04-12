from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Outlets, Products

from .forms import OutletForm, ProductForm

# import googlemaps
# gmaps = googlemaps.Client(key='AlzaSyCn5pUJqC_L_7Br0rKKpLXxMgKvPKN-aGE')
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

def show_products(request):
    items = Products.objects.all()
    if request.method == "POST":
        key = request.POST.get('key')
        items = Products.objects.get(id=key)
        
    map = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2952.0594696309417!2d90.39785852559339!3d23.87422598409942!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755c43bb8c21a3b%3A0xf37e844834c635fa!2sMascot%20Plaza%2C%20Uttara%2C%20Dhaka!5e0!3m2!1sen!2sbd!4v1649771713356!5m2!1sen!2sbd" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">'
    return render(request, 'App_Admin/index.html', context={'items':items, 'latitude':23.815414889088338, 'longitude':90.36611284885306, 'map':map})


def all_outlets(request):
    outlets = Outlets.objects.all()
    return render(request, 'App_Admin/all_outlets.html', context={'outlets':outlets})

def add_outlets(request):
    form = OutletForm()

    if request.method == "POST":
        form = OutletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Outlet Added successfully!', extra_tags='success')
            return HttpResponseRedirect(reverse('App_Admin:add_outlets'))

    return render(request, 'App_Admin/add_outlets.html', context={'form':form})

def edit_outlet(request,outlet_id):
    outlet = Outlets.objects.get(id=outlet_id)
    form = OutletForm(instance=outlet)

    if request.method == "POST":
        form = OutletForm(request.POST, request.FILES, instance=outlet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated successfully!', extra_tags='success')
            return HttpResponseRedirect(reverse('App_Admin:all_outlets'))
    return render(request, 'App_Admin/edit_outlet.html', context={'form':form})
