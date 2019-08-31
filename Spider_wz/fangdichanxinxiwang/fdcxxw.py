# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('http://www.hbczfdc.com/TMSFW/HPMS/ProjectInfoList.aspx')  # 打开界面
i=1;

def page_zh(i):
    tds = driver.find_element_by_id('PageNavigator1_txtNewPageIndex')
    # 清空文本方法
    tds.clear()
    tds.send_keys(i)
    print("第" + tds.get_attribute("value") + "页")
    driver.find_element_by_id('PageNavigator1_LnkBtnGoto').click()
    # 获取页面html
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
    href_ = soup.select('td[align="left"] a')
    for line in href_:
        print('http://www.hbczfdc.com/TMSFW'+line['href'].replace('..',''))
        # # 连接数据库
        connect = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='cz_fdcxxw_wq')
        # 获取游标
        cursor = connect.cursor()
        # 插入数据
        sql = "INSERT INTO  cz_wq_url (url) VALUES ( '%s')"
        data ='http://www.hbczfdc.com/TMSFW'+line['href'].replace('..','')
        cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        connect.close()
    if (i < 117):
        i=i+1
        page_zh(i)
    else:
        print("本次采集结束!!!")

page_zh(i)
# 关闭浏览器（selenium）
# driver.quit()

