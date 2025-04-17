import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

# 读取数据
df = pd.read_excel('policy_data.xlsx')

# 数据预处理
# 假设数据已处理完毕，这里需要根据实际数据调整特征工程
# 特征工程
# 删除无关字段并处理分类变量
df = df.drop(['policy_id', 'policy_start_date', 'policy_end_date'], axis=1)

# 分离特征和目标变量
try:
    X = pd.get_dummies(df.drop('renewal', axis=1))
    Y = df['renewal'].map({'是':1, '否':0}).astype(int)
    print('特征列示例：', X.columns[:5])
    print('目标变量分布：\n', Y.value_counts())
except Exception as e:
    print('数据处理错误：', str(e))
    raise

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 训练模型
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 预测与评估
y_pred = model.predict(X_test)
print(f'准确率: {accuracy_score(y_test, y_pred):.2%}')
print(f'AUC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1]):.2%}')

# 系数可视化
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 系数可视化
coefficients = pd.Series(model.coef_[0], index=X.columns)
coefficients_abs = coefficients.abs().sort_values(ascending=False)
top20_features = coefficients_abs.head(20).index
coefficients_top20 = coefficients[top20_features].sort_values()

plt.figure(figsize=(10,6))
colors = ['green' if x >0 else 'red' for x in coefficients_top20]
coefficients_top20.plot(kind='barh', color=colors)

plt.title('Top20逻辑回归特征系数（绿色正相关/红色负相关）')
plt.xlabel('系数值')
plt.ylabel('特征')
plt.grid(axis='x', linestyle='--')
max_val = max(abs(coefficients_top20))
plt.xlim(-max_val*1.1, max_val*1.1)

# 添加数值标签
for i, v in enumerate(coefficients_top20):
    plt.text(v, i, f'{v:.2f}', color='black', ha='left' if v <0 else 'right')

plt.tight_layout()
plt.savefig('coefficients_plot.png')
plt.close()
plt.show()