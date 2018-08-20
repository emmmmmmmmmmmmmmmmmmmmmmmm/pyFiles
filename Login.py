from flask import Flask,request
import pymysql,json
app = Flask(__name__)
db = pymysql.connect('localhost','root','demo12345','android',charset = 'utf8')
cursor = db.cursor()
@app.route('/login',methods=['POST'])
def login():
    args = request.json
    phone = args['phone']
    password = args['password']
    return select(phone,password)
def select(phone,password):
    sql_select_phone = 'select phone from login where phone = %s' % str(phone)
    cursor.execute(sql_select_phone)
    res = cursor.fetchone()
    sql_select_password = 'select password from login where phone = %s' % str(phone)
    if res != None:
        cursor.execute(sql_select_password)
        code = cursor.fetchone()
        if code[0] == password:
            return json.dumps({'code':0,'msg':'操作成功','datas':[]})
        else:
            return json.dumps({'code':10002,'msg':'操作失败','datas':[]})
    else:
        dict = {'code':10001,'msg':'操作失败','datas':[]}
        return json.dumps(dict)
@app.route('/register',methods=['POST'])
def register():
    args = request.json
    phone = args['phone']
    password = args['password']
    return  register(phone,password)
def register(phone,password):
    sql_select_phone = 'select phone from login where phone = %s' % str(phone)
    cursor.execute(sql_select_phone)
    res = cursor.fetchone()
    sql_insert = 'insert into login (phone,password) values ("%s","%s")'%(str(phone),str(password))
    if res == None:
        cursor.execute(sql_insert)
        db.commit()
        dict = {'code': 0, 'msg': '操作成功', 'datas': []}
        return json.dumps(dict)
    else:
        dict = {'code': 10003, 'msg': '操作失败', 'datas': []}
        return json.dumps(dict)

@app.route('/update',methods=['POST'])
def update():
    args = request.json
    phone = args['phone']
    password = args['password']
    return  update(phone,password)
def update(phone,password):
    sql_select_phone = 'select phone from login where phone = %s' % str(phone)
    cursor.execute(sql_select_phone)
    res = cursor.fetchone()
    sql_update = 'update login set password = %s where phone = %s'%(str(password),str(phone))
    if res !=None:
        cursor.execute(sql_update)
        db.commit()
        dict = {'code': 0, 'msg': '操作成功', 'datas': []}
        return json.dumps(dict)
    else:
        dict = {'code': 10004, 'msg': '操作失败', 'datas': []}
        return json.dumps(dict)

if __name__ == '__main__':
    app.run()

