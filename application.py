from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! from Azure check mysql"

@app.route("/con")
def con():
    conn = pymysql.connect(host='my01.winhost.com', user='ashishwp', password='patelashwp',db='mysql_19668_wp1')
    cu = conn.cursor()
    sql =("select * from stockmast")
    cu.execute(sql)
    data = cu.fetchone()
    return data
