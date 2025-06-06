from django.db import models

# Create your models here.

class bookRecord(models.Model):
    id = models.IntegerField(primary_key= True)
    bookName =  models.CharField( max_length=150) 
    bookAuthor= models.CharField( max_length=100)
    bookYear = models.IntegerField()
    isbn = models.IntegerField()
    isActive = models.BooleanField()
    
    
    
    
    
    
    
'''
[auth]
        changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
    makemigrations
    migrate
        optimizemigration
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
    startapp
    startproject
        test
        testserver

[sessions]
        clearsessions

[staticfiles]
        collectstatic
        findstatic
    runserver
'''