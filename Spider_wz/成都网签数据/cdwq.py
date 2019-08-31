# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from selenium import webdriver
driver = webdriver.Chrome()  # 打开火狐浏览器
driver.get('http://zw.cdzj.chengdu.gov.cn/py/SCXX/Default.aspx?action=ucSCXXShowNew')  # 打开界面
i = 1

def page_zh(i):
    print('==================================第{}页==========================='.format(i))
    if(i!= 1):
        driver.find_element_by_id('ID_ucSCXXShowNew_UcPager1_btnNewNext').click()
    # 获取页面html
    html = driver.page_source
    res = pq(html)
    table_main = res('#ID_ucSCXXShowNew_gridView>tbody>tr')
    for l in range(1,table_main.length):
        # 预售现售号
        yxsh = table_main.eq(l).children('td').eq(0).text()
        #项目名称
        xmmc = table_main.eq(l).children('td').eq(1).text()
        #行政区域
        xzqy = table_main.eq(l).children('td').eq(2).text()
        #项目地址
        xmdz = table_main.eq(l).children('td').eq(3).text()
        #房屋用途
        fwyt = table_main.eq(l).children('td').eq(4).text()
        #开发商
        kfs = table_main.eq(l).children('td').eq(5).text()
        #预售面积（平方米）
        ysmj = table_main.eq(l).children('td').eq(6).text()
        #预售日期
        ysrq = table_main.eq(l).children('td').eq(7).text()
        #销售代理
        xsdl = table_main.eq(l).children('td').eq(8).text()
        #监管银行
        jgyh = table_main.eq(l).children('td').eq(9).text()
        #备注
        bz = table_main.eq(l).children('td').eq(10).text()
        print(xmmc)
        connect = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='chengdu_wq')
        # 获取游标
        cursor = connect.cursor()
        # 插入数据
        sql = "INSERT INTO cd_wq (yxsh, xmmc, xzqy, xmdz, fwyt, kfs, ysmj, ysrq, xsdl, jgyh, bz) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
        data = (yxsh, xmmc, xzqy, xmdz, fwyt, kfs, ysmj, ysrq, xsdl, jgyh, bz)
        cursor.execute(sql,data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        connect.close()

    if (i < 1583):
        i=i+1
        page_zh(i)
    else:
        print("本次采集结束!!!")

page_zh(i)
# 关闭浏览器（selenium）
# driver.quit()

