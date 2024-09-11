import django_filters
from api.models import Book
from .filters import BookFilter
from rest_framework import generics
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
