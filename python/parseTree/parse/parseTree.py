#coding:utf-8
import os
import dataTree
from string import Template

header = u"""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>tree</title>
    <link type="text/css" href="css/tree.css" rel="stylesheet"/>
</head>

<body>
<div id="treeBlock" class="treeBlock">
    <ul>
"""
footer = u"""
    </ul>
</div>

<script type="text/javascript" src="js/tree.js"></script>
</body>    
</html>
"""
treeRoot = u"""
        <li class="treeRoot" >
            <h3 class="treeRoot-title"> ${title} </h3>
            <ul class="treeNodeBlock"> ${nodeBlock} 
            </ul>
        </li>
"""
def parseTree(data):
    treeNodeBlock = []
    treeNodeLen = len(data["node"])
    for n in range(0, treeNodeLen):
        treeNodeTmp = Template("\n                <li>${node}</li>") 
        treeNodeContent = treeNodeTmp.substitute(node = data["node"][n])
        treeNodeBlock.append(treeNodeContent)
        
        if type(data["node"][n]) == dict:
            #递归生成节点
            treeNodeBlock[n] = parseTree(data["node"][n])

    treeRootTmp = Template(treeRoot)
    treeRootContent = treeRootTmp.substitute(title = data["title"], nodeBlock = "".join(treeNodeBlock))
    return "".join(treeRootContent)

def parseTreeArr(dataArr):
    treeArrContent = []
    treeArrLen = len(dataArr)
    for m in range(0, treeArrLen):
        treeArrContent.append(parseTree(dataArr[m]))
    return "".join(treeArrContent)

dataArr = dataTree.dataArr
html = []
html.append(header)
html.append(parseTreeArr(dataArr))
html.append(footer)

htmlStr = "".join(html)

f = file("../html/treeAuto.html", "w")
f.write(htmlStr)
f.close()
