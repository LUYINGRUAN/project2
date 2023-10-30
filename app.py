from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# 读取 bars_info.xlsx 文件
df = pd.read_excel('bars_info.xlsx')

# 将评分字段中的空值替换为0
df['Rating'].fillna(0, inplace=True)

api_key = ''

@app.route('/')
def index():
    return render_template('index.html', df=df, api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)

