from django.db import models
class Employee(models.Model):
    EmpNum = models.IntegerField(null=True, blank=True)
    EmpName = models.CharField(max_length=64,null=True, blank=True)
    EmpSal = models.IntegerField(null=True, blank=True)
    EmpEmail = models.EmailField(max_length=64,null=True, blank=True)
    EmpDesc = models.TextField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.EmpName
