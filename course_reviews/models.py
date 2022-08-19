from django.db import models


class CourseReviews(models.Model):
    """ Model that stores course reviews """
    name = models.CharField(max_length=254, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=254, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        self.name
    
    