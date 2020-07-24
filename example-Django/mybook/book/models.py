from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField()

    def __str__(self):
        return self.title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    comment = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
