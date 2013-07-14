#coding:utf-8
from HTMLParser import HTMLParser
import urllib2
import re
#import os
#获取一个静态网页上的所有图片（css中的背景图除外）
#config url
SITE_URL = "http://www.digu.com/board/detail/tjwpelhut22pn"


#根据url获取网页的内容
def getHtml(url):
    file = urllib2.urlopen(url)
    content = file.read()
    return content

#保证src是绝对路径,图片格式正确
def checkSrc(src):
    suffix = re.search(r'.*\.(.{3})', src).group(1)
    if not re.search(r'png|jpg|gif', suffix):
        return None
    if not re.search(r'http://', src):
        base =  re.search(r'http.*com', SITE_URL).group(0)
        src = base + "/" + src
    return src
#根据src获取图片的名字
def getImgName(src):
    arr = re.split(r'/', src)
    imgName = arr[len(arr)-1]
    return imgName

#print getImgName('http://www.baidu.com/img/baidu_sylogo1.gif')

#保存图片到img下
def saveImg(src, name):
    img = urllib2.urlopen(src)
    local = file("img/" + name, "wb")
    local.write(img.read())


#saveImg("http://www.baidu.com/img/baidu_sylogo1.gif", "1.gif")

#解析html文档类
class GetImg (HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return None
        for name, value in attrs:
            if name != "src":
                continue
            src = checkSrc(value)
            if not src:
                continue
            print src
            imgName = getImgName(src)
            saveImg(src, imgName)

if __name__ == "__main__":
    get = GetImg()
    #get.feed('<html><img src="xx.jpg"/></html>')
    print 'start ...'
    context = getHtml(SITE_URL)
    open('getHtml.html', 'w').write(context)
    get.feed(context)
    print '...end '
