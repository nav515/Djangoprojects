from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse

from .mixins import HttpResponseMixin

from django.views.generic import View
# Create your views here.
def home(request):
    emp_data= {'Name':'Naveen Gopagani',
               'Phone_num':9010579202,
               'Add':'Hyderabad'}
    
    #resp = json.dumps(emp_data)
    #print(type(resp()))
    #return HttpResponse(resp,content_type='application/json')

    print(type(emp_data))
    return JsonResponse(emp_data)

class jsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**Kwargs):
        emp_data= {'Name':'Naveen Gopagani',
               'Phone_num':9010579202,
               'Add':'Hyderabad',
               'Get':'This is GET'}
        json_data = json.dumps(emp_data)    
        #return JsonResponse(json_data,safe=False)
        return self.render_to_http_response(json_data)
    
    def post(request,*args,**Kwargs):
        emp_data= json.dumps({'post':'This is POST'})
        return HttpResponse(emp_data,content_type='application/json')
    
    def put(request,*args,**Kwargs):
        emp_data= {'Name':'Naveen Gopagani',
               'Phone_num':9010579202,
               'Add':'Hyderabad',
               'put':'This is PUT'}
        return JsonResponse(emp_data)
    
    def delete(request,*args,**Kwargs):
        emp_data= {'Name':'Naveen Gopagani',
               'Phone_num':9010579202,
               'Add':'Hyderabad',
               'delete':'This is Delete'}
        return JsonResponse(emp_data)
    



