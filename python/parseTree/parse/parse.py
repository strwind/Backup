#coding=utf-8
from string import Template
import data

#读取模板文件
tmpStr = file("../template/index.template.html").read()
#替换模板中的变量
htmlTmp = Template(tmpStr)
#htmlContent = htmlTmp.substitute(title = data.index["title"] , h1 = data.index["h1"])
htmlContent = htmlTmp.substitute(data.index)
print htmlContent
#生成网页
htmlFile = file("../html/index.html", "w")
htmlFile.write(htmlContent)
htmlFile.close() 

