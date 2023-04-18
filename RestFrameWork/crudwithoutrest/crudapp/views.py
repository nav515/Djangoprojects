from django.shortcuts import render,HttpResponse
from . import models
import json
from django.views.generic import View
from django.core.serializers import serialize
from .mixins import serializeMixin
from .mixins import HttpRespMixix
from .utils import is_json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . forms import EmployeeForm

# Create your views here.
def home(request):
    return HttpResponse('Naveen')

class EmpjsonCBV(serializeMixin,View):
    def get(self,request,id,*args,**kwargs):

        try:
            emp = models.Employee.objects.get(id=id) 

        except models.Employee.DoesNotExist:
            emp_data = json.dumps({'msg':'The Required id is not Exist'})
            #emp_data = serialize('json',[emp,],fields=(id,'ename','eemail','eadd'))
            return HttpResponse(emp_data,content_type = 'application/json',status=400)

        else:
            emp_data = self.serialize([emp,])
            emp_data = json.dumps(emp_data)        
            return HttpResponse(emp_data,content_type = 'application/json',status=200)
        
@method_decorator(csrf_exempt, name='dispatch')   
class EmpListCBV(HttpRespMixix,View):
    def get(request,*args,**kwargs):
        qs = models.Employee.objects.all() 
        
        emp_data = serialize('json',qs)
        py_dict = json.loads(emp_data)

        final_list=[]
        for obj in py_dict:
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",obj['fields'])
            final_list.append(obj['fields'])

        emp_data = json.dumps(final_list)
        return HttpResponse(emp_data,content_type = 'application/json')
    

    def post(self,request,*args,**kwargs):
        #json_data= json.dumps({'msg':'this is from Post'})
        #return self.HttpResponse(json_data,content_type='appilcation/json',status=200)
        data = request.body
        is_jsonvalid = is_json(data)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",is_jsonvalid)
        if is_jsonvalid:
            emp_data = json.loads(data)
            form = EmployeeForm(emp_data)
            if form.is_valid():
                form.save(commit=True)
                #json_data= json.dumps({'msg':'you provided json data only'})
                json_data= json.dumps({'msg':'user created'})
                return self.render_to_http_res(json_data)
            elif form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_res(json_data,status=400)
        # else:
        #     json_data = json.dumps({'msg':'not json data'})
        #     return self.render_to_http_res(json_data,status=400)
    
