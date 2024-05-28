from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'publisher_profile', null= True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'author_profile', null= True)
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'books')
    genre = models.CharField(max_length=12)
    publication_date = models.DateField(auto_now_add=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name= 'books')
    rating = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Store(models.Model):
    name = models.CharField(max_length= 25, blank=True)
    books = models.ManyToManyField(Book, related_name= 'stores')

    def __str__(self):
        return self.name
