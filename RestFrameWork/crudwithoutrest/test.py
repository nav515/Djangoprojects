import requests
import json

Base_url = 'http://127.0.0.1:8000/'
End_point = 'api/'
# id = input('enter id')
print("################################## Get the Single User Data ")
def get_res(id):
    res = requests.get(Base_url + End_point+str(id))
    print(res)
    data = res.json()
    print(res.status_code)
    print(data)
get_res(3)

print("################################## Get the all Users Data ")

def get_all():
    res = requests.get(Base_url + End_point)
    print(res)
    data = res.json()
    print(res.status_code)
    print(data)
get_all()

print("################################## posting the data ")


def post_fun():
    emp= {'ename':'krish',
          'eemail':'krishc@gmail.com',
          'esal': '100',
          'eadd':'ban'}
    
    res= requests.post(Base_url + End_point,json.dumps(emp))
    data = res.json()
    print(res.status_code)
    print(data)
post_fun()



def put_fun(id):
    emp = {
          'ename':'naveen',
          'esal': '22000',
          'eadd':'india'
          }
    res = requests.put(Base_url + End_point+str(id)+'/',json.dumps(emp))
    data = res.json()
    print(res.status_code)
    print(data)
put_fun(11)

def delete_fun(id):
    res = requests.delete(Base_url + End_point+str(id)+'/')
    data = res.json()
    print(res.status_code)
    print(data)
delete_fun(7)


    





