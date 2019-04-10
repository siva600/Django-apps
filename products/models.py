from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=False)  # null = True, default= True

    # blank has to deal with how the field is rendered and null has to deal
    # with the database.

    # this method make sure any changes in the url also effect the changes
    # where ever the url dependencies are used.
    # e.g the main url products/id/ is used in product_list.html as href.
    # so any changes in main url also effect the other dependencies.

    def get_absolute_url(self):
        # name spacing is done in products urls. so write as products:
        return reverse("products:product-detail", kwargs={"id": self.id})
