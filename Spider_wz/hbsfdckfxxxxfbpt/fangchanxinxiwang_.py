# coding:utf-8
from selenium import webdriver
import time
import mysql.connector
from bs4 import BeautifulSoup
from lxml import etree
import os
i=993
jsonData = []
def main(jsonData,i):
    print(jsonData[i])
    driver=webdriver.Firefox()
    # driver=webdriver.PhantomJS(executable_path="C:\Python36\Scripts\phantomjs.exe")
    driver.get(jsonData[i])
    time.sleep(4)
    print(str(i)+driver.find_element_by_css_selector(".TB_Body2").get_attribute("innerHTML"))
    # 获取页面html
    file = open('D:\FC\s'+str(i+1)+'.txt', 'w')
    file.close()
    html = driver.find_element_by_css_selector(".TB_Body2").get_attribute("innerHTML")
    fos = open('D:\FC\s'+str(i+1)+'.txt', "w", encoding="utf-8")
    fos.write(html)
    fos.close()
    driver.quit()
    i+=1
    main(jsonData, i)

# 打开数据库连接
db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='hb_fcw')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT url FROM hb_fcw_url"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   # 打印结果

   for row in results:
       result = {}
       result = row[0].decode('utf-8')
       jsonData.append(result)

   main(jsonData,i)
   print(len(results))
except:
   print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
