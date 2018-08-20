# -*- coding: utf-8 -*-

import pymysql
import json
import sys


class DbConnect(object):
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()

    def login(self, phone, password):
        sql_select_phone = 'select phone from login where phone = %s' % str(phone)
        self.cursor.execute(sql_select_phone)
        res = self.cursor.fetchone()
        sql_select_password = 'select password from login where phone = %s' % str(phone)
        try:
            if res != None:
                self.cursor.execute(sql_select_password)
                code = self.cursor.fetchone()
                if code[0] == password:
                    return json.dumps({'code': 0, 'msg': '操作成功', 'datas': []})
                else:
                    return json.dumps({'code': 10002, 'msg': '操作失败', 'datas': []})
            else:
                dict = {'code': 10001, 'msg': '操作失败', 'datas': []}
                return json.dumps(dict)
        except:
            raise Exception
    def register(self, phone, password):
        sql_select_phone = 'select phone from login where phone = %s' % str(phone)
        self.cursor.execute(sql_select_phone)
        res = self.cursor.fetchone()
        sql_insert = 'insert into login (phone,password) values ("%s","%s")' % (str(phone), str(password))
        try:
            if res == None:
                self.cursor.execute(sql_insert)
                self.con.commit()
                dict = {'code': 0, 'msg': '操作成功', 'datas': []}
                return json.dumps(dict)
            else:
                dict = {'code': 10003, 'msg': '操作失败', 'datas': []}
                return json.dumps(dict)
        except:
            raise Exception
    def modify(self, phone, password):
        sql_select_phone = 'select phone from login where phone = %s' % str(phone)
        self.cursor.execute(sql_select_phone)
        res = self.cursor.fetchone()
        sql_update = 'update login set password = %s where phone = %s' % (str(password), str(phone))
        try:
            if res != None:
                self.cursor.execute(sql_update)
                self.con.commit()
                dict = {'code': 0, 'msg': '操作成功', 'datas': []}
                return json.dumps(dict)
            else:
                dict = {'code': 10004, 'msg': '操作失败', 'datas': []}
                return json.dumps(dict)
        except:
            raise Exception

    def transfor(self, opr ,phone, password):
        try:
            if opr == "login":
                return self.login(phone, password)
            elif opr == "register":
                return self.register(phone, password)
            elif opr == "modify":
                return self.modify(phone, password)
        except:
            self.con.rollback()
        finally:
            self.close()
    #关闭连接
    def close(self):
        pass
        # if (self.cursor):
        #     self.cursor.close()
        # if (self.con):
        #     self.con.close()
if __name__ == '__main__':
    opr = "login"
    con = pymysql.Connect(host='127.0.0.1', port=3306, db='android', user='root',
                          passwd='demo12345', charset='utf8')
    dbConnect = DbConnect(con)
    dbConnect.transfor("login", "15717914505", "666666")
