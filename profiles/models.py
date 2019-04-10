from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    last_name = models.CharField(max_length=120, blank=False, null=False)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    email = models.EmailField(max_length=254,blank=False)

