from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# 配置MySQL数据库连接
db = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="51job"
)

# 创建游标
cursor = db.cursor()


# 定义路由
@app.route('/')
def index():
    # 执行SQL查询
    cursor.execute("SELECT * FROM your_table_name")

    # 获取所有数据
    data = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    db.close()

    # 将数据传递给HTML模板
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

