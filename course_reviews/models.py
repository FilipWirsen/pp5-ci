from django.db import models


class CourseReview(models.Model):
    """ Model that stores course reviews """
    name = models.CharField(max_length=254, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=254, null=False, blank=False)
    text = models.TextField()
    address = models.CharField(max_length=254, null=False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    website = models.CharField(max_length=254, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
