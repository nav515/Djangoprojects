from django.contrib import admin
from . models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmpNum','EmpName','EmpSal','EmpEmail','EmpDesc','Emp_image']

admin.site.register(Employee,EmployeeAdmin)
