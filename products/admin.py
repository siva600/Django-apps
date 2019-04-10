from django.contrib import admin

# Register your models here.

from .models import Product

# this is relative import because admin.py and models.py are in the same directory.

admin.site.register(Product)



