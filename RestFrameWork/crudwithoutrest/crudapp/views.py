from django.shortcuts import render,HttpResponse
from . import models
import json
from django.views.generic import View
from django.core.serializers import serialize
from .mixins import serializeMixin
from .mixins import HttpRespMixix
from .utils import is_json,get_object_by_id

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . forms import EmployeeForm

# Create your views here.


def home(request):
    return HttpResponse('Naveen')



@method_decorator(csrf_exempt, name='dispatch')   
class EmpjsonCBV(serializeMixin,HttpRespMixix,View):
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

     
    
    def put(self,request,id,*args,**kwars):
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        emp = get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No matched record to perfom updation'})
            return HttpResponse(json_data,content_type = 'application/json',status=404)
        data = request.body
        vaild_json = is_json(data) 
        if not vaild_json:
            json_data = json.dumps({'msg':'pls send valid json_data only'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        provided_data = json.loads(data)    
        original_data = {
            'ename':emp.ename, 
            'eemail':emp.eemail,
            'esal':emp.esal,
            'eadd':emp.eadd
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        if form.is_valid():
                form.save(commit=True)
                #json_data= json.dumps({'msg':'you provided json data only'})
                print('################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                json_data= json.dumps({'msg':'updated Succussfully'})
                #return HttpResponse(json_data,content_type='application/json',status=200)
                return self.render_to_http_res(json_data)
        if form.errors:
                json_data = json.dumps(form.errors)
                #return HttpResponse(json_data,content_type='application/json',status=400)
                return self.render_to_http_res(json_data,status=400)

    def delete(self,request,id,*args,**kwargs):
        emp = get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'there is no data to delete on this id'})
            return self.render_to_http_res(json_data,status=400)
        print(emp.ename,emp.eemail,emp.esal,emp.eadd)
        status,deleted_item= emp.delete() #tuple unpacking here
        print(status,'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        print(deleted_item,'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        if status ==1:
            json_data = json.dumps({'msg':'resource deleted'})
            return self.render_to_http_res(json_data)
        json_data = json.dumps({'msg':'unable to delete pls try'})
        return self.render_to_http_res(json_data)











                    
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
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_res(json_data,status=400)
        # else:
        #     json_data = json.dumps({'msg':'not json data'})
        #     return self.render_to_http_res(json_data,status=400)
    
