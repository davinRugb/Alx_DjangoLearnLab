from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.DateField()
    published_at = models.CharField(max_length=50)

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name