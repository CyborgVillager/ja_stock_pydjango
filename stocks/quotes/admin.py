from django.contrib import admin
# import models.py
from .models import Stock

# regist models into the admin page
admin.site.register(Stock)


