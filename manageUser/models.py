from django.db import models

# Create your models here.


class user (models.Model):
    id = models.IntegerField(primary_key=True)
    userTyp = models.CharField(max_length=10)
    userGender = models.CharField(max_length=10)
    userFirstName = models.CharField(max_length=150)
    userSecondName = models.CharField(max_length=150)
    userStreetName = models.CharField(max_length=150)
    userHouseNumber = models.IntegerField()
    userZipCode = models.IntegerField()
    userCityName = models.CharField(max_length=150)
    userEmail = models.EmailField()
    userPhone = models.IntegerField()
    userBirthdate= models.DateTimeField()
    isActive =models.BooleanField()
    