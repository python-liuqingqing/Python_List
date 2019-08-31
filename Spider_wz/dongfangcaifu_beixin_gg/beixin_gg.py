# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
import threading
from selenium import webdriver
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('http://data.eastmoney.com/notices/stock/000786.html')  # 打开界面
i=1
pages=25;
def page_zh(i):
    driver.find_element_by_id('PageContgopage').clear()
    driver.find_element_by_id('PageContgopage').send_keys(i)
    driver.find_element_by_class_name('btn_link').click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
    href_ = soup.select('#dt_1 a')
    for line in href_:
        print("http://data.eastmoney.com" + line['href'])
        # 连接数据库
        connect = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='dfcf_beixin_url')
        # 获取游标
        cursor = connect.cursor()
        # 插入数据
        sql = "INSERT INTO  beixin_url (url) VALUES ( '%s')"
        data = "http://data.eastmoney.com"+line['href']
        cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        connect.close()
    if (i < pages):
        i = i + 1
        threading.Timer(5,  page_zh, [i]).start()
    else:
        print("本次采集结束!!!")
page_zh(1)
