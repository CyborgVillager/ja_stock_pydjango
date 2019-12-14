from django.db import models
#db information

# Create your models here.
class Stock(models.Model):
    # ticker symbol char length
    ticker = models.CharField(max_length=10)

    # admin info for ticker registri.
    def __str__(self):
        return self.ticker

    #once done with db info, python manage.py makemigrations &  python manage.py migrate