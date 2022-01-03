from django.contrib import admin
from .models import Book, BookNumber, Character, Author


# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'published', 'is_published', 'cover', 'number']
    list_filter = ['published']
    list_display = ['title', 'description', 'price', 'published']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
