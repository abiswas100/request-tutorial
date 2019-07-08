import requests
payload = {'page':2, 'count':3}
r = requests.get('http://httpbin.org/get',params=payload)

print(r.text)
print(r.url)