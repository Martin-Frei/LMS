from django.db import models

# Create your models here.



class alert(models.Model):
    id = models.IntegerField(primary_key=True)
    alertTitle = models.CharField(max_length=150)
    alertText = models.TextField()
    alertType = models.CharField(max_length=15)
    alertTimestamp = models.DateTimeField()
    isActive = models.BooleanField()