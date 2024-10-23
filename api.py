import requests
import json

url = "https://api.atinternet.io/v3/data/getData-m_unique_visitors%22%5D,%22space%22:%7B%22s%22:%5B612602%5D%7D,%22period%22:%7B%22p1%22:%5B%7B%22type%22:%22D%22,%22start%22:%222024-01-01%22,%22end%22:%222024-09-30%22%7D%5D%7D,%22max-results%22:50,%22page-num%22:1,%22options%22:%7B%22ignore_null_properties%22:true%7D%7D"

payload = '''{
    "columns": ["device_type","m_visits","m_users"],
    "sort": ["-m_visits"],
    "space": {"s": [123456789]},
    "period": {"p1": [{"type": "D","start": "2019-10-24","end": "2019-10-24"}]},
    "max-results": 50,
    "page-num": 1
}'''

headers = {
    'x-api-key': "69cd02807d93_da7cdb65f1e9542bc921cb7d809e577f90e0454a",
    'Content-Type': "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.status_code)
print(response.text)
