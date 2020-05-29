import requests

r = requests.get("https://monhapp.com")
print(r.status_code)
print(r.ok)
