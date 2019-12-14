from django import forms
# connecting to models.py
from .models import Stock

# new class for the form / field using models.py & add_stock.html

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']