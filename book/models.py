from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=20)


class Author(models.Model):
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(blank=True)


class Book(models.Model):
    title = models.CharField(max_length=30, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=12)
    publication_date = models.DateField(auto_now_add=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    rating = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)


class Reviews(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
