import requests
import json

url = "https://api.atinternet.io/v3/data/getData"

payload = '''{
    "columns": ["device_type","m_visits","m_users"],
    "sort": ["-m_visits"],
    "space": {"s": [123456789]},
    "period": {"p1": [{"type": "D","start": "2019-10-24","end": "2019-10-24"}]},
    "max-results": 50,
    "page-num": 1
}'''

headers = {
    'x-api-key': "df00358496fb",
    'Content-Type': "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.status_code)
print(response.text)
