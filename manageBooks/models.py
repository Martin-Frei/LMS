from django.db import models

# Create your models here.

class bookRecord(models.Model):
    id = models.IntegerField(primary_key= True)
    bookName =  models.CharField( max_length=150) 
    bookAuthor= models.CharField( max_length=100)
    bookYear = models.IntegerField(max_length=4)
    isbn = models.IntegerField(max_length=13)
    isActive = models.BooleanField()