from flask import Flask, render_template
import json

app = Flask(__name__)

# 示例数据（需替换为真实数据源）
with open('decision_tree_rules.txt') as f:
    decision_rules = f.read()

@app.route('/')
def dashboard():
    return render_template('dashboard.html',
                          renewal_rate=72.4,
                          feature_importance={
                              '逻辑回归': ['年龄', '保单日期', '婚姻状态', '家庭人数'],
                              '决策树': ['年龄', '婚姻状态', '家庭人数', '保单日期']
                          },
                          decision_rules=decision_rules)

if __name__ == '__main__':
    app.run(debug=True)