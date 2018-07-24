import requests
r = requests.get('https://google.com/')
r.status_code
r.history

print(r)
