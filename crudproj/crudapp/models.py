from django.db import models
class Employee(models.Model):
    EmpNum = models.IntegerField()
    EmpName = models.CharField(max_length=64)
    EmpSal = models.IntegerField()
    EmpEmail = models.EmailField(max_length=64)
    EmpDesc = models.TextField(max_length=100)
    Emp_image = models.ImageField(upload_to = 'images')
    def __str__(self):
        return self.EmpName
