import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsonCBV'


res_get= requests.get(BASE_URL+END_POINT)
res_get1 = res_get.json()

res_post =requests.post(BASE_URL+END_POINT)
res_post1 = res_post.json()

res_put =requests.put(BASE_URL+END_POINT)
res_put1 = res_put.json()

res_delete =requests.delete(BASE_URL+END_POINT)
res_delete1 = res_delete.json()



print(res_get1)
print(res_post1)
print(res_put1)
print(res_delete1)