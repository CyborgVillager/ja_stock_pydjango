from django.urls import path
from . import views


urlpatterns = [
    # accessing home.html from views.py
    path('', views.home, name='home')
]