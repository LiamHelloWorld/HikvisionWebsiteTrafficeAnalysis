import os
import glob
import pandas as pd
import numpy as np
import xlsxwriter as xlsx

def find_latest_csv(directory='.'):
    """
    查找当前目录下最新的 CSV 文件。
    """
    csv_files = glob.glob(os.path.join(directory, '*.csv'))
    if not csv_files:
        print("没有找到CSV文件")
        return None
    return max(csv_files, key=os.path.getmtime)

def load_and_clean_csv(file_path, keep_values):
    """
    加载 CSV 文件，并根据指定的值过滤数据和删除特定列。
    """
    df = pd.read_csv(file_path, sep=';')
    
    # 过滤数据
    df_cleaned = df[df.iloc[:, 0].isin(keep_values)].copy()

    if df_cleaned.empty:
        print("没有找到匹配的行，清洗后的数据为空。")
        return None

    df_cleaned = df_cleaned.drop([col for col in df_cleaned.columns if 'Difference' in col], axis=1)
    return df_cleaned


def convert_columns_to_numeric(df, columns):
    """
    将指定的列转换为数值类型。
    """
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def calculate_summary(df, columns):
    """
    计算指定列的汇总行，并根据公式计算变化比例。
    """
    sum_row = df[columns].sum()

    variation_between_visits = (sum_row["Visits (p1)"] - sum_row["Visits (p2)"]) / sum_row["Visits (p2)"]
    variation_between_visitors = (sum_row["Visitors (p1)"] - sum_row["Visitors (p2)"]) / sum_row["Visitors (p2)"]
    variation_between_page_views = (sum_row["Page views (p1)"] - sum_row["Page views (p2)"]) / sum_row["Page views (p2)"]

    new_row = {
        df.columns[0]: "Sum",  # 第一列
        "Visits (p1)": sum_row["Visits (p1)"],
        "Visits (p2)": sum_row["Visits (p2)"],
        "Variation between Visits (p2) and Visits (p1)": variation_between_visits,
        "Visitors (p1)": sum_row["Visitors (p1)"],
        "Visitors (p2)": sum_row["Visitors (p2)"],
        "Variation between Visitors (p2) and Visitors (p1)": variation_between_visitors,
        "Page views (p1)": sum_row["Page views (p1)"],
        "Page views (p2)": sum_row["Page views (p2)"],
        "Variation between Page views (p2) and Page views (p1)": variation_between_page_views
    }

    # 使用 pd.concat() 添加新行
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    
    return df

def split_tables(df):
    """
    将数据分为三个表格：Visits, Visitors 和 Page Views，动态识别第一列的列名。
    """
    # 获取第一列的列名
    first_column_name = df.columns[0]
    
    # 根据动态列名分割表格
    df_visits = df[[first_column_name, "Visits (p1)", "Visits (p2)", "Variation between Visits (p2) and Visits (p1)"]]
    df_visitors = df[[first_column_name, "Visitors (p1)", "Visitors (p2)", "Variation between Visitors (p2) and Visitors (p1)"]]
    df_page_views = df[[first_column_name, "Page views (p1)", "Page views (p2)", "Variation between Page views (p2) and Page views (p1)"]]
    
    return df_visits, df_visitors, df_page_views


def save_to_excel(df_visits, df_visitors, df_page_views, filename='result_tables.xlsx'):
    """
    将 Visits, Visitors 和 Page Views 三个 DataFrame 保存到同一个 Excel 文件的不同 sheet 中。
    """
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        # 写入不同的 sheet
        df_visits.to_excel(writer, sheet_name='Visits', index=False)
        df_visitors.to_excel(writer, sheet_name='Visitors', index=False)
        df_page_views.to_excel(writer, sheet_name='Page Views', index=False)
    
    print(f"表格已成功保存到 {filename}")

def main():
    # 查找最新的 CSV 文件
    latest_csv = find_latest_csv()

    if latest_csv:
        # 保留的第一列的值
        keep_values = [
            "ip-products", "turbo-hd-products", "video-intercom-products", "software", "accessories",
            "access-control-products", "display-and-control", "alarm-products", "transmission",
            "thermal-products", "its-products", "onboard-security"
        ]

        # 加载和清洗数据
        df_cleaned = load_and_clean_csv(latest_csv, keep_values)

        # 转换数值列
        columns_to_sum = ["Visits (p1)", "Visits (p2)", "Visitors (p1)", "Visitors (p2)", "Page views (p1)", "Page views (p2)"]
        df_cleaned = convert_columns_to_numeric(df_cleaned, columns_to_sum)

        # 计算汇总行并更新数据框
        df_cleaned = calculate_summary(df_cleaned, columns_to_sum)

        # 拆分表格
        df_visits, df_visitors, df_page_views = split_tables(df_cleaned)

        # 将结果保存到 Excel 文件的不同 sheet 中
        save_to_excel(df_visits, df_visitors, df_page_views, filename='result_tables.xlsx')

if __name__ == "__main__":
    main()
