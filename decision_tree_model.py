import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from read_data import load_insurance_data  # 复用数据加载模块

# 中文字体配置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载并预处理数据
df = load_insurance_data('policy_data.xlsx')
X = df.drop('renewal', axis=1)
y = df['renewal']

# 划分训练测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建决策树模型
dtc = DecisionTreeClassifier(max_depth=3, random_state=42)
dtc.fit(X_train, y_train)

# 模型评估
y_pred = dtc.predict(X_test)
print(f"测试集准确率：{accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))

# 可视化决策树
plt.figure(figsize=(20,10))
plot_tree(dtc, 
          feature_names=X.columns.tolist(),
          class_names=['不续保', '续保'],
          filled=True,
          rounded=True)
plt.savefig('decision_tree.png', dpi=300, bbox_inches='tight')
print("决策树可视化已保存为 decision_tree.png")

# 生成决策树文本规则
chinese_features = {
    'age': '年龄',
    'gender': '性别',
    'policy_type': '保单类型',
    'premium': '保费',
    'claim_history': '理赔历史',
    'region': '地区'
}
tree_rules = export_text(dtc, 
                       feature_names=[chinese_features.get(col, col) for col in X.columns],
                       show_weights=True)

# 保存并输出文本规则
with open('decision_tree_rules.txt', 'w', encoding='utf-8') as f:
    f.write(tree_rules)
print("\n决策树文本规则已保存为 decision_tree_rules.txt")
print("="*50)
print(tree_rules)