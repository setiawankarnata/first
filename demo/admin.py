from django.contrib import admin
from .models import Book


# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'published']
    list_filter = ['published']
    list_display = ['title', 'description', 'price', 'published']
    search_fields = ['title', 'description']
