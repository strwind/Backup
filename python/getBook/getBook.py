#!/usr/bin/env python
# coding=utf-8
#获取盗墓笔记全集小说
from bs4 import BeautifulSoup
import urllib2
import os

#得到一篇文章
#根据url解析文本 并保存
def parseAndSave (url, filename, title):
	html = BeautifulSoup(urllib2.urlopen(url).read())
	data = html.find('div',{'class':'content'})
	#获取到段落 不递归
	pArr = data.findAll(name ='p', attrs= {"class":""}, recursive=False)
	textArr = []
	for p in pArr:
		textArr.append(unicode(p.contents[0]))
	texts = "\n".join(textArr)
	f = file(filename, 'w')
	f.write('*******'+ title +'*******\n'+ texts)
	f.close()

#得到1部晓说 即一个文件夹
#根据一部晓说的dom包装器
def getOnePart(partDom):
	tb = partDom.table
	trs = tb.findAll('tr')
	for tr in trs:
		if 3 == len(tr):
			dirname = tr.td.center.h2.string
			#没有目录 则新建之
			if not os.path.isdir(dirname):
				os.makedirs(unicode(dirname))
		elif 7 == len(tr):
			tds = tr.findAll('td')
			for td in tds:
				try:
					url = td.a['href']
				except:
					continue
				chap = td.a.string
				print chap
				filename = dirname + os.sep + chap + '.txt'
				parseAndSave(url, filename, chap)

#得到一共八部晓说
#初始化
def init(url):
	quanji = BeautifulSoup(urllib2.urlopen(url).read())
	mulus = quanji.findAll('div',{'class':'mulu'})
	for mulu in mulus:
		getOnePart(mulu)

if __name__ == "__main__":
	base_url = r'http://www.daomubiji.com/dao-mu-bi-ji-quan-ji/'
	init(base_url)

