from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    comment = models.CharField(max_length=100)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
