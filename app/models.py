from django.db import models

class AdmUser(models.Model):
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

class Book(models.Model):
    bookTitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    pages = models.IntegerField()




