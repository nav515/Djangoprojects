from django.db import models

# Create your models here.

class Employee(models.Model):
    # the name of class represent table name in database
    ename = models.CharField(max_length=255)
    eemail = models.EmailField()
    esal = models.IntegerField()
    eadd = models.CharField(max_length=200)
    def __str__(self):
        return self.ename
    
