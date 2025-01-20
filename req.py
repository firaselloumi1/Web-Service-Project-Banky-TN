import requests

url = "https://api.repl.it/cus/slsnlcA1!"
response = requests.post(url)
print(response.status_code)
print(response.json())
