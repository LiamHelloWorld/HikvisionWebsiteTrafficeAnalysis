import http.client

# 创建 HTTPS 连接
conn = http.client.HTTPSConnection("api.atinternet.io")

# 定义请求体（payload）
payload = '''{
    "columns": [
        "device_type",
        "m_visits",
        "m_users"
    ],
    "sort": [
        "-m_visits"
    ],
    "space": {
        "s": [123456789]
    },
    "period": {
        "p1": [
            {
                "type": "D",
                "start": "2019-10-24",
                "end": "2019-10-24"
            }
        ]
    },
    "max-results": 50,
    "page-num": 1
}'''

# 设置请求头，确保传递正确的 Content-Type
headers = {
    'x-api-key': "69cd02807d93_da7cdb65f1e9542bc921cb7d809e577f90e0454a",  # 替换为实际的 API key
    'Content-type': "application/json"
}

# 发送 POST 请求并将参数传递到请求体中
conn.request("POST", "/v3/data/getData", body=payload, headers=headers)

# 获取响应
res = conn.getresponse()
data = res.read()

# 打印返回的数据
print(data.decode("utf-8"))

# 关闭连接
conn.close()
