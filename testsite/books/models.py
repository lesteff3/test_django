from django.db import models
from django.conf import settings


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
#