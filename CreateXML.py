from xml.dom.minidom import Document
doc = Document()  #创建DOM文档对象
root = doc.createElement('root') #创建根元素
#DOCUMENT.setAttribute('xsi:noNamespaceSchemaLocation','DOCUMENT.xsd')#引用本地XML Schema
doc.appendChild(root)
############item:Python处理XML之Minidom################
user_name = doc.createElement('user_name')
user_name_text = doc.createTextNode(' I am Stone') #元素内容写入
user_name.appendChild(user_name_text)
root.appendChild(user_name)

pass_word = doc.createElement('pass_word')
pass_word_text = doc.createTextNode('666666') #元素内容写入
pass_word.appendChild(pass_word_text)
root.appendChild(pass_word)

########### 将DOM对象doc写入文件
f = open('AutoCreate.xml','w')
#f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8'))
doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')
f.close()



