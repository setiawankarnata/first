from django.db import models


class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=60)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=4, default=0, decimal_places=2, blank=True)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.FileField(upload_to="covers/")

    def __str__(self):
        return self.title
