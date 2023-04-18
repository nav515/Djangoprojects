import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsonCBV'


res_get= requests.get(BASE_URL+END_POINT)
res_get = res_get.json()

res_post =requests.post(BASE_URL+END_POINT)
res_post = res_post.json()

res_put =requests.put(BASE_URL+END_POINT)
res_put = res_put.json()

res_delete =requests.delete(BASE_URL+END_POINT)
res_delete = res_delete.json()



print(res_get)
print(res_post)
print(res_put)
print(res_delete)