import DbConnect
from flask import Flask,request,make_response
import pymysql,json

from xml.dom.minidom import parseString

import CreateXML

app = Flask(__name__)


if __name__ == '__main__':
    con = pymysql.Connect(host='127.0.0.1', port=3306, db='android', user='root',
                          passwd='demo12345', charset='utf8')
    dbConnect = DbConnect.DbConnect(con)
    #登录:
    @app.route('/login',methods=['POST'])
    def login():
        args = request.json
        phone = args['phone']
        password = args['password']
        return dbConnect.transfor("login", phone, password)
    # 注册:
    @app.route('/register', methods=['POST'])
    def register():
        args = request.json
        phone = args['phone']
        password = args['password']
        return dbConnect.transfor("register", phone, password)
    #更新:
    @app.route('/update', methods=['POST'])
    def update():
        args = request.json
        phone = args['phone']
        password = args['password']
        return dbConnect.transfor("modify", phone, password)


    def get_nodevalue(node, index=0):
        return node.childNodes[index].nodeValue

    @app.route('/', methods=['POST'])
    def testXML():
        #args = request.args
        #print(args.get("xml"))
        args = request.data
        print(args)
        xmlStr = args.decode('utf-8');
        dom= parseString(xmlStr)
        print(dom.getElementsByTagName("root")[0].getElementsByTagName("user_name")[0].childNodes[0].nodeValue)
        # 使用minidom解析器打开 XML 文档
        # DOMTree = ET.parse   #ET.parse("xml.xml")
        # root = DOMTree.getroot();
        # user_name = root.findall("user_name");
        # print(user_name[0].text)
        res = make_response(json.dumps({"code":0,"msg":"操作成功","datas":[]}))
        #设置了响应头
        res.headers['Content-Type'] = "text/xml";

        return '<?xml version="1.0" encoding="utf-8"?><root><user_name>'+"IoI"+'</user_name><pass_word>888888</pass_word></root>'
    #启动服务器：
    app.run(host='0.0.0.0', port=5000)


    #做下笔记：
    #获取客户端get请求的数据：request.args    request.values
    #获取客户端post请求的json字符串数据：request.json
    #获取客户端post请求的xml字符串数据：request.data,取到的数据是二进制数据 .decode('utf-8')转成正常数据