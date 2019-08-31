# coding=utf-8
import time
import datetime
import mysql.connector
import re
import redis
from bs4 import BeautifulSoup
from selenium import webdriver
from pyquery import PyQuery as pq
import requests
import time
driver = webdriver.Chrome()  # 打开火狐浏览器
driver.get('https://yth.weihai.gov.cn/whythgcPortal/PortalWH/FinishUnionList.aspx')  # 打开界面
i = 1
time.sleep(3)
def t_main(i):
    print('=========================第{}页========================='.format(i))
    html = driver.find_element_by_id('ctl00_MainContent_rgProjectList_ctl00').get_attribute('innerHTML')
    h = pq(html)
    jg = h('tbody').children('tr')
    for h in range(jg.length):
        # 项目名称
        xmmc = jg.eq(h).children('td').eq(0).text()
        #工程名称
        gcmc = jg.eq(h).children('td').eq(1).text()
        #建设单位
        jsdw = jg.eq(h).children('td').eq(2).text()
        #勘察单位
        kcdw = jg.eq(h).children('td').eq(3).text()
        #设计单位
        sjdw = jg.eq(h).children('td').eq(4).text()
        #施工单位
        sgdw = jg.eq(h).children('td').eq(5).text()
        #项目经理
        xmjl =jg.eq(h).children('td').eq(6).text()
        #项目总监
        xmzj = jg.eq(h).children('td').eq(7).text()
        #审核日期
        shrq = jg.eq(h).children('td').eq(8).text()
        #区域
        qy = jg.eq(h).children('td').eq(9).text()
        print(xmmc)

        db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='weihai')
        cursor = db.cursor()
        insert_color = (
            "INSERT INTO wh_jgys (xmmc,gcmc,jsdw,kcdw,sjdw,sgdw,xmjl,xmzj,shrq,qy)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data_color = (xmmc,gcmc,jsdw,kcdw,sjdw,sgdw,xmjl,xmzj,shrq,qy)
        cursor.execute(insert_color, data_color)
        db.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        db.close()

    driver.find_element_by_class_name('rgPageNext').click()
    time.sleep(3)
    if(i<64):
        i=i+1
        t_main(i)

if __name__ == '__main__':
    t_main(i)