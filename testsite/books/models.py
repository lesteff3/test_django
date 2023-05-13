from django.db import models
from django.conf import settings


class Author(models.Model):
    name_author = models.CharField(max_length=100)

    def __str__(self):
        return self.name_author


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name='bookss'
    )
    count = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)


    def get_percent_sell(self):
        percent_sell = round((self.stock / self.count) * 100, 2)
        return percent_sell




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

