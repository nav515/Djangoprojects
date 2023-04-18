import json
from django.core.serializers import serialize
from django.shortcuts import render,HttpResponse

class serializeMixin(object):
    def serialize(self,qs):
        json_data = serialize('json',qs)
        p_dict = json.loads(json_data)

        final_list = []
        for obj in p_dict:
            emp = obj['fields']
            final_list.append(emp)
        json_data = json.dumps(final_list)
        return json_data
    
class HttpRespMixix(object):
    def render_to_http_res(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)