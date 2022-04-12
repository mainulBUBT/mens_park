from django.urls import path
from . import views

app_name = 'App_Admin'

urlpatterns = [
    path("", views.show_products, name="show_products"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.admin_login, name="login"),
    path('logout/', views.admin_logout, name="logout"),
    path('add_products/', views.add_products, name='add_products'),
    path('all_products/', views.all_products, name="all_products"),
    path('edit_product/<int:product_id>', views.edit_product, name="edit_product"),
    path('delete_product/<int:product_id>', views.delete_product, name="delete_product"),
    path('all_outlets/', views.all_outlets, name='all_outlets'),
    path('add_outlets/', views.add_outlets, name='add_outlets'),
     path('edit_outlet/<int:outlet_id>', views.edit_outlet, name="edit_outlet"),
]
