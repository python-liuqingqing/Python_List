# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('http://jzsg.hebjs.gov.cn//Foundation/easyUI/Grid/ShowGrid.aspx?GridKey=890f5ac6-50f1-4cf2-bb6f-aa94a45f61dc')  # 打开界面
time.sleep(15)
i=1;

def page_zh(i):
    print(i)
    if(i>1):
        driver.find_element_by_css_selector(".rgPageNext").click()
    time.sleep(10)
    # 获取页面html
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
    href_ = soup.select('div[style="color:#519ADD;font-size:16px;font-weight:600;cursor:pointer;"]')
    for line in href_:
        print("http://jzsg.hebjs.gov.cn/jwkfbProject/HeBeiRealtyDev/Pages/Publish/Publish_ItemInfo1.aspx?PrjNum="+line['onclick'][14:33]+"&Types=0")
        # # # 连接数据库
        connect = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='hb_fcw')
        # 获取游标
        cursor = connect.cursor()
        # 插入数据
        sql = "INSERT INTO  fdckf_hb (url) VALUES ( '%s')"
        data ="http://jzsg.hebjs.gov.cn/jwkfbProject/HeBeiRealtyDev/Pages/Publish/Publish_ItemInfo1.aspx?PrjNum="+line['onclick'][14:33]+"&Types=0"
        cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        connect.close()
    if (i < 52):
        i=i+1
        page_zh(i)
    else:
        print("本次采集结束!!!")

page_zh(i)
# 关闭浏览器（selenium）
# driver.quit()

