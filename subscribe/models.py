from django.db import models

# Create your models here.
class Subscribers(models.Model):
    """
    Subscriber model
    """

    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "subscribers"

    def __str__(self):
        return self.email
