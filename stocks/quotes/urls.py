from django.urls import path
from . import views


urlpatterns = [
    # accessing home.html from views.py
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock/', views.delete_stock, name='delete_stock'),
]