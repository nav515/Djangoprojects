from django.contrib import admin
from . models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmpNum','EmpName','EmpSal','EmpEmail','EmpDesc']
    ordering = ('EmpNum',)

admin.site.register(Employee,EmployeeAdmin)
