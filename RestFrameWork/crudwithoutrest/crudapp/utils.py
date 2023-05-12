import json
from .models import Employee
def is_json(data):
    try:
        p_data = json.loads(data)
        #so here changing the json to dict so 
        valid = True
    except ValueError:
        valid = False
    return valid

def get_object_by_id(id):
    try:
        emp= Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        emp=None
    return emp


