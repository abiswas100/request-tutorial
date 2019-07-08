import requests
payload = {'username':'Avhi20', 'password':'testing'}
r = requests.post('http://httpbin.org/post',data=payload)


print(r.json())

r_dict = r.json()

print(r_dict['form'])
