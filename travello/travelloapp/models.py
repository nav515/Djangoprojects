from django.db import models

# Create your models here.
class traveller_det(models.Model):
    tr_name = models.CharField(max_length=128,blank=True)
    tr_age = models.IntegerField('tr_age', null=False,blank=True, default=00000)
    tr_gender = models.CharField(max_length=6,blank=True)
    tr_phnum = models.IntegerField('tr_phnum', null=False,blank=True, default=00000)
    tr_aadar = models.IntegerField(primary_key=True,blank=True)
    tr_image = models.ImageField(upload_to='images',blank=True)
    def __str__(self):
        return self.tr_name

