from django.urls import path
from . import views

app_name = 'App_Admin'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.admin_login, name="login"),
    path('logout/', views.admin_logout, name="logout"),
    path('add_products/', views.add_products, name='add_products'),
]
