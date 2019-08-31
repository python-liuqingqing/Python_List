#coding=utf-8
import urllib.request
import requests
from docx import Document
import requests
from lxml import etree

for page in range(3):
    # 网址
    url="http://www.mofangge.com/html/qDetail/04/c2/201406/p0mec204288883.html"
    # 对象
    r=requests.get(url)
    # 状态码
    print(r)
    fp = open('{}.doc'.format("a"), 'wb')
    fp.write(r.content)
    fp.close()
