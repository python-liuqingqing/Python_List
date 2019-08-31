#coding:utf-8
import requests
import urllib
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium import webdriver
import os
import sys
sys.setrecursionlimit(10000)

driver = webdriver.Chrome()
driver.get('https://www.jianyu360.com/jylab/supsearch/proposedProject.html')
time.sleep(8)

jsonData1=[]
jsonData2=[]
jsonData3=[]
jsonData4=[]
jsonData5=[]
jsonData6=[]
jsonData7=[]
jsonData8=[]
jsonData9=[]
l=0

def main(jsonData1,jsonData2,jsonData3,jsonData4,jsonData5,jsonData6,jsonData7,jsonData8,jsonData9,l):
    print(l)
    print("https://www.jianyu360.com/article/content/"+ id+".html")
    js = 'window.open("https://www.jianyu360.com/article/content/' + id+'.html");'
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
        driver.close()
        driver.switch_to_window(handles[0])
        import random
        if(l%20==0):
            time.sleep(random.randint(6,9))
        time.sleep(random.randint(1,3))
        l += 1
        main(jsonData1,jsonData2,jsonData3,jsonData4,jsonData5,jsonData6,jsonData7,jsonData8,jsonData9,l)
    except:
        time.sleep(random.randint(1,3))
        l += 1
        main(jsonData1,jsonData2,jsonData3,jsonData4,jsonData5,jsonData6,jsonData7,jsonData8,jsonData9,l)





if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='master')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM 360doc"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果

    for row in results:
        a1 = row[1].decode('utf-8')
        a2 = row[2].decode('utf-8')
        a3 = row[3].decode('utf-8')
        a4 = row[1].decode('utf-8')
        a5 = row[2].decode('utf-8')
        a6 = row[3].decode('utf-8')
        a7 = row[1].decode('utf-8')
        a8 = row[2].decode('utf-8')
        a9 = row[3].decode('utf-8')
        jsonData1.append()
        jsonData2.append()
        jsonData3.append()
        jsonData4.append()
        jsonData5.append()
        jsonData6.append()
        jsonData7.append()
        jsonData8.append()
        jsonData9.append()
    main(jsonData1,jsonData2,jsonData3,jsonData4,jsonData5,jsonData6,jsonData7,jsonData8,jsonData9,l)
    print(len(results))
    db.close()