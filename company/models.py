
from django.db import models

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length = 10)
    field = models.CharField(max_length = 10)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.ticker
