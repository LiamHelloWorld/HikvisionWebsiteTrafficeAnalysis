import pandas as pd
import json

def transform_data():
    # 从本地文件中读取 JSON 数据
    with open('piano_data.json', 'r') as f:
        data = json.load(f)
    
    # 打印原始数据
    print("原始数据: ", data)
    
    # 将 JSON 数据转换为 pandas 数据框
    df = pd.DataFrame(data['results'])  # 假设 'results' 是我们感兴趣的部分
    df_transformed = df[['field1', 'field2', 'field3']]  # 选择感兴趣的字段进行转换
    
    # 可以对数据进行更多的处理，如清洗、聚合等
    df_transformed['new_field'] = df_transformed['field1'] * 2  # 示例处理操作

    # 保存处理后的数据到本地
    df_transformed.to_csv('transformed_piano_data.csv', index=False)
    print("数据已转换并保存")

transform_data()
