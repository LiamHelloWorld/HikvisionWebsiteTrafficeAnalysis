import requests
import json

url = "https://api.atinternet.io/v3/data/getData?param=%7B%22columns%22:%5B%22event_url%22,%22event_name%22,%22hit_time_utc%22,%22m_unique_visitors%22%5D,%22sort%22:%5B%22-m_unique_visitors%22%5D,%22space%22:%7B%22s%22:%5B612602%5D%7D,%22period%22:%7B%22p1%22:%5B%7B%22type%22:%22D%22,%22start%22:%222024-01-01%22,%22end%22:%222024-09-30%22%7D%5D%7D,%22max-results%22:50,%22page-num%22:1,%22options%22:%7B%22ignore_null_properties%22:true%7D%7D"

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
