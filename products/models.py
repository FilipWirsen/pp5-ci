from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=6, decimal_places=2,
                                              null=True, blank=True, default=0)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2,
                                           null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    @property
    def get_discounted_price(self):
        if self.discount_percentage:
            self.discounted_price = self.price - self.price * self.discount_percentage
            return self.discounted_price


class Review(models.Model):
    """ Model for raiting products """
    user = models.ForeignKey(UserProfile, related_name='review',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='review',
                                on_delete=models.CASCADE)
    user_rating = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, blank=False)
    review_message = models.CharField(max_length=254, null=True, blank=True)
                                      
