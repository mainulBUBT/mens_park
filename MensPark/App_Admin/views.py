from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request, 'App_Admin/login.html')

def dashboard(request):
    return render(request, 'App_Admin/dashboard.html')
