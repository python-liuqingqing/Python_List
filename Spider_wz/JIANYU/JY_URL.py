#coding=utf-8
from pymongo import MongoClient
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from selenium import webdriver
import mysql.connector
import time
from docx.oxml.ns import qn
chromeOptions = webdriver.ChromeOptions()
# 设置代理
# chromeOptions.add_argument("--proxy-server=http://117.191.11.74:80")
driver = webdriver.Chrome()#chrome_options = chromeOptions
driver.get('https://www.jianyu360.com/jylab/supsearch/proposedProject.html')
time.sleep(8)
import json
#建立MongoDB数据库连接
client = MongoClient('localhost',27017)
#连接所需数据库,test为数据库名
db=client.JianYu
#连接所用集合，也就是我们通常所说的表，test为表名
collection=db.jianyu_url_2019
#接下里就可以用collection来完成对数据库表的一些操作
#查找集合中所有数据
for item in collection.find():
    print(item)
    for a in range(len(item['list'])):
        print(a)
        id = item['list'][a]['_id']
        area = item['list'][a]['area']
        href = item['list'][a]['href']
        try:
            industry = item['list'][a]['industry']
        except:
            industry = ""

        publishtime = item['list'][a]['publishtime']
        try:
            s_subscopeclass = item['list'][a]['s_subscopeclass']
        except:
            s_subscopeclass = ""
        try:
            subtype = item['list'][a]['subtype']
        except:
            subtype = ""

        title = item['list'][a]['title']
        try:
            toptype = item['list'][a]['toptype']
        except:
            toptype = ""
        print("https://www.jianyu360.com/article/content/"+ id+".html")
        js = 'window.open("https://www.jianyu360.com/article/content/' + id+'.html");'
        # js = 'window.open("https://www.jianyu360.com/article/content/ABCY2FJfy44MDY7EmRhcHUJJzACHj1mZnB%2FPC8nKy4gXmhzcCNUCfI%3D.html")'
        driver.execute_script(js)
        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        for handle in handles:  # 切换窗口（切换到搜狗）
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
        try:
            html = driver.find_element_by_class_name('biddetail-content').get_attribute('innerHTML')
            nr_text = driver.find_element_by_class_name('biddetail-content').text
            import re
            pat = re.compile("中标日期：" + '(.*?)' + "\n", re.S)
            zbsj = pat.findall(nr_text)
            print(zbsj)
            # print(nr_text)
            # 创建并写入word文档
            import docx
            j_time = driver.find_element_by_class_name('com-time').text
            j_yhref = driver.find_element_by_class_name('com-original').get_attribute('href')
            # 创建内存中的word文档对象
            # file = docx.Document()
            # file.styles['Normal'].font.name = u'宋体'
            # file.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
            # # 写入若干段落
            # file.add_paragraph(nr_text)
            # # 保存
            # file.save("{}.docx".format(j_time+title))
            # soup = BeautifulSoup(html, 'lxml')  # 对html进行解析

            data = {
                'id':id,
                'area':area,
                'zbsj':zbsj,
                'href':href,
                'industry':industry,
                'publishtime':publishtime,
                's_subscopeclass':s_subscopeclass,
                'subtype':subtype,
                'title':title,
                'toptype':toptype,
                'j_time':j_time,
                'j_yhref':j_yhref,
                'nr_text':nr_text
            }
            print(data)

            import pymongo
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["JianYu"]
            mycol = mydb["JianYu_XQ_2019"]
            x = mycol.insert_one(data)

            driver.close()
            driver.switch_to_window(handles[0])
            import random
            if(a%20==0):
                time.sleep(random.randint(10,19))
            time.sleep(random.randint(6,13))
        except:
            time.sleep(random.randint(5,9))
            continue



