
#!/usr/bin/python3

import json
from flask import Flask
from flask import request
import pymysql
import sys

app = Flask(__name__)

db = pymysql.connect("127.0.0.1", "root", "demo12345", "android", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

def insertSql(stuName,stuTel,stuAddress):
    # SQL 插入语句
    sql = 'insert into stu_tbl(stu_name,stu_tel, stu_address) values("%s", "%s", "%s")' % \
             (stuName, stuTel,stuAddress)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        print("数据插入成功")
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生异常，则回滚
        info = sys.exc_info()
        print(info[0], ":", info[1])
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()

def updateSql(stuName,id):
    # SQL 插入语句
    sql = "UPDATE stu_tbl SET stu_name = '%s' WHERE stu_id = '%d'" % (stuName,id)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        print("数据更新成功")
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生异常，则回滚
        info = sys.exc_info()
        print(info[0], ":", info[1])
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()

def delSql(id):
    # SQL 插入语句
    sql = "DELETE FROM stu_tbl WHERE stu_id = '%d'" % (id)
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        print("数据删除成功")
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生异常，则回滚
        info = sys.exc_info()
        print(info[0], ":", info[1])
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()

def selectSql():
    # SQL 插入语句
    sql = "SELECT * FROM stu_tbl "
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        backs = []
        data = {}
        for res in results:
            back = {}
            back['stu_id'] = res[0]
            back['stu_name'] = res[1]
            back['stu_tel'] = res[2]
            back['stu_address'] = res[3]
            backs.append(back)
        data['code'] = 0
        data['msg'] = "操作成功"
        data['datas'] = backs
        jsonStr = json.dumps(data)
        return  jsonStr
        db.commit()
    except:
        # 如果发生异常，则回滚
        info = sys.exc_info()
        print(info[0], ":", info[1])
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()

@app.route('/',methods=['GET'])
def version_list():
    args = request.args
    # insertSql('oooo', '13666027011','福建省厦门市湖里区殿前路口')
    # updateSql("I am tools",5)
    # delSql(5)
    selectSql()
    return selectSql()

@app.route('/post/datas',methods=['POST'])
def execute_datas():
    args = request.json
    print(args)
    return selectSql() #json.dumps(args)

@app.route('/app/sms_login',methods=['POST'])
def appSmsLogin():
    args = request.json
    try:
        # 执行sql语句
        sql = 'select user_code from user_tbl where user_name=15717914505'

        #"select user_code from user_tbl where user_name = '%s'" % (id)
        cursor.execute(sql)
        user_code = cursor.fetchall()
        #jsonStr = json.dumps(data)
        print(user_code)
        db.commit()
    except:
        # 如果发生异常，则回滚
        info = sys.exc_info()
        print(info[0], ":", info[1])
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()
    return json.dumps(args)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5678)
