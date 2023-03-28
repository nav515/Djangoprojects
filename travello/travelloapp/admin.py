from django.contrib import admin
from . import models
# Register your models here.
class tr_detAdmin(admin.ModelAdmin):
    list_display = ['tr_name','tr_age','tr_gender','tr_phnum','tr_aadar','tr_image']
admin.site.register(models.traveller_det,tr_detAdmin)
