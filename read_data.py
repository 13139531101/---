import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_insurance_data(file_path):
    # 设置支持中文的字体
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    df = pd.read_excel(file_path)
    
    # 转换日期字段为数值类型
    date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    for col in date_cols:
        df[col] = (df[col] - pd.Timestamp('1970-01-01')) // pd.Timedelta('1D')
    
    # 处理所有日期类型字段
    date_cols = df.select_dtypes(include=['datetime64']).columns
    if not date_cols.empty:
        df = df.drop(date_cols, axis=1)
        print(f'已移除日期类型字段：{list(date_cols)}')
    
    # 强制类型转换
    categorical_cols = ['gender', 'policy_type', 'claim_history', 'region']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype(str)
    
    # 数据预处理
    # 自动处理所有分类特征
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        if col in ['gender', 'claim_history']:  # 特殊处理有明确映射的字段
            if col == 'gender':
                df[col] = df[col].map({'男':0, '女':1})
            elif col == 'claim_history':
                df[col] = df[col].map({'无':0, '有':1})
        else:
            df[col] = df[col].astype(str).astype('category').cat.codes
    # 最终类型验证
    print('\n最终数据类型验证：')
    for dtype in df.dtypes:
        if not np.issubdtype(dtype, np.number):
            print(f'发现非数值类型列：{dtype}')
    
    # 调试输出预处理结果
    print('\n预处理后数据样例：')
    print(df.head())
    print('\n各列数据类型：')
    print(df.dtypes)
    return df

if __name__ == '__main__':
    df = load_insurance_data('policy_data.xlsx')
    
    # 打印前5行数据
    print('前5行数据：')
    print(df.head(5))

    # 打印所有列名
    print('\n数据列名：')
    print(df.columns.tolist())

    # 生成统计摘要
    print('\n统计摘要：')
    print(df.describe())

    # 检查缺失值
    print('\n缺失值统计：')
    print(df.isnull().sum())

    # 绘制分布直方图
    plt.figure(figsize=(12,6))
    cols = ['age', 'policy_type', 'claim_history']
    for i,col in enumerate(cols,1):
        plt.subplot(1,3,i)
        sns.histplot(df[col], kde=True)
        plt.title(f'{col}分布')
    plt.tight_layout()

    # 生成相关性矩阵
    plt.figure(figsize=(10,8))
    numeric_cols = df.select_dtypes(include=['number']).columns
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('字段间相关性矩阵')
    plt.savefig('correlation_matrix.png')
    plt.close()

    # 显示图形
    plt.show()