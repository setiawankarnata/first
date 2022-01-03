from django.db import models


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.isbn_10


class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=60)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=4, default=0, decimal_places=2, blank=True)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.FileField(upload_to="covers/", blank=True)
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE,
                                  related_name='booknumber2book')

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book2character")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name="book2author")

    def __str__(self):
        return self.name
