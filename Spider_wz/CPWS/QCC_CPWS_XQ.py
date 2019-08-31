#coding:utf-8
import requests
import urllib
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium import webdriver
import os
from pyquery import PyQuery as pq
import sys
sys.setrecursionlimit(10000)
from docx.oxml.ns import qn

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=1683fb937674bb-077cc91827ef82-10306653-fa000-1683fb93768355; zg_did=%7B%22did%22%3A%20%221683fb937e39e2-01f19c3143046f-10306653-fa000-1683fb937e5a63%22%7D; _uab_collina=154725732987486420475217; saveFpTip=true; zg_63e87cf22c3e4816a30bfbae9ded4af2=%7B%22sid%22%3A%201547629712155%2C%22updated%22%3A%201547630289092%2C%22info%22%3A%201547629712158%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%7D; acw_tc=968a62a415499379127792651e5128fea7d301c156944600b4f9618954; QCCSESSID=ilg056mn1pic646t3s826frdo0; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1551661605,1551666103,1551667337,1551668093; CNZZDATA1254842228=702832566-1547255991-https%253A%252F%252Fwww.baidu.com%252F%7C1551666315; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201551669939042%2C%22updated%22%3A%201551670481800%2C%22info%22%3A%201551659095401%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%228450661249f59172fa197e771a876891%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1551670482',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
url = 'https://www.qichacha.com/wenshuDetail_c42b3bbcf107fb86e19f247dc7ea0c7a.html'
r = pq(requests.get(url,headers=headers).text)
data = r('#searchlist').text()
#创建并写入word文档
import docx
#创建内存中的word文档对象
file=docx.Document()
file.styles['Normal'].font.name = u'宋体'
file.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
#写入若干段落
file.add_paragraph(data)
#保存
file.save("{}.docx".format("data"))