from django.db import models

# Create your models here.

class rentTime(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn = models.IntegerField()
    issuerId = models.IntegerField()
    userId = models.IntegerField()
    rentDate = models.DateTimeField(auto_now = True)
    rentDuration =models.DateTimeField()
    isActive = models.BooleanField()