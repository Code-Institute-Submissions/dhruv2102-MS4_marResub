from django.db import models


# Create your models here.
class Testimonials(models.Model):
    """
    Testimonial model
    """

    name = models.CharField(max_length=254)
    testimony = models.TextField()

    def __str__(self):
        return self.name
