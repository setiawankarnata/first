from rest_framework import serializers
from .models import Book, BookNumber, Character, Author


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    book2character = CharacterSerializer(many=True)
    book2author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number', 'book2character',
                  'book2author']


class BookMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title']
