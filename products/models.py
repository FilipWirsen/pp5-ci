from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    raiting = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    @property
    def get_discounted_price(self):
        self.price = self.price - self.price * self.discount_percentage
        return self.price