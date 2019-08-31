# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from selenium import webdriver
i=1;

def page_zh(i):
    print(i)
    driver = webdriver.Firefox()  # 打开火狐浏览器
    driver.get('http://www.shui5.cn/article/HeBeiShengCaiShuiFaGui/158_'+str(i)+'.html')  # 打开界面
    time.sleep(1)
    # 获取页面html
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
    href_ = soup.select('.arcList li p a')
    for line in href_:
        print("http://www.shui5.cn"+line['href'])
        # 连接数据库
        connect = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='master')
        # 获取游标
        cursor = connect.cursor()
        # 插入数据
        sql = "INSERT INTO  yqy_url (url) VALUES ( '%s')"
        data ="http://www.shui5.cn"+line['href']
        cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        connect.close()
    driver.quit()
    if (i <= 7):
        i=i+1
        page_zh(i)
    else:
        print("本次采集结束!!!")

page_zh(i)
# 关闭浏览器（selenium）

