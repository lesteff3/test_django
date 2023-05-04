from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'