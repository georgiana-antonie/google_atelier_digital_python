# import requests
# import json
#
# url = "http://127.0.0.1:8000/my_api/api/"
#
# payload = json.dumps({
#   "city": "Brasov",
#   "country": "Romania"
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.json())

import requests

url = "https://v6.exchangerate-api.com/v6/d01788f6764c212c4285d31a/latest/USD"

payload = ""
headers = {
  'Authorization': 'Token d01788f6764c212c4285d31a'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()['conversion_rates']['EUR'])