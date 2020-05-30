
from flask import Flask
from db import db_connector
import  random
#hello.py
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/create')
def insert():
    sql = 'insert into user (username,password) value("{name}","123")'.format(name=random.randint(300,500))
    return db_connector(sql)

@app.route('/read')
def select():
    sql = 'select * from user'
    return db_connector(sql)

@app.route('/update')
def update():
    sql = "UPDATE user SET username = '{random}' WHERE id=1".format(random=random.randint(1,100))
    return db_connector(sql)

@app.route('/delete')
def delete():
    sql = "delete from user where id=1"
    return db_connector(sql)

if __name__ == '__main__':
    app.run()