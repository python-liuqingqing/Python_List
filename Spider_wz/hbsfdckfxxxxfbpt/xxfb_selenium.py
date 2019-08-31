# coding:utf-8
from selenium import webdriver
import time
import mysql.connector
from bs4 import BeautifulSoup
from lxml import etree
import os
i=1093
jsonData = []
def main(jsonData,i):
    print(jsonData[i])
    driver=webdriver.Firefox()
    driver.get(jsonData[i])
    # time.sleep(10)
    # 获取页面html
    file = open('D:\HB\labels'+str(i+1)+'.txt', 'w')
    file.close()
    html = driver.page_source
    fos = open('D:\HB\labels'+str(i+1)+'.txt', "w", encoding="utf-8")
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
sql = "SELECT url FROM fdckf_hb"
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



