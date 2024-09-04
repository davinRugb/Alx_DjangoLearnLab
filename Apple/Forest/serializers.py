from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "id", "title", "author", "published_date"

def validate(self, data):
        if len(data["author"]) < 5:
            raise serializers.ValidationError("Name must be at least 5 characters long.")
        return data
