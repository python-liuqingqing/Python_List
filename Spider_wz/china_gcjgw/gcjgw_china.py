# -*- coding: UTF-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium import webdriver
import sys
sys.setrecursionlimit(10000)
jsonData=[]
l=28285
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('https://www.zh818.com/members/memlogin.aspx')
time.sleep(2)
driver.find_element_by_id('username').send_keys('13181818506-2')
driver.find_element_by_id('password').send_keys('317773')
driver.find_element_by_id('LinkButton1').click()
time.sleep(2)
def main(jsonData,l):
    print("第"+str(l)+"条")
    print(jsonData[l])
    js = 'window.open("'+jsonData[l]+'");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换）
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(3)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'lxml')

    try:
        driver.find_element_by_id('zoom')
        print("存在")
        trs = soup.select("#zoom table tbody tr")
        ulist = []
        for tr in range(1, len(trs)):
            ui = []
            for td in trs[tr]:
                ui.append(td.string)
            ulist.append(ui)
        for i in range(len(ulist)):
            try:
                title = driver.find_element_by_id('content-title').text
                sj = (driver.find_element_by_id('content-copyright').text).replace('www.zh818.com','').replace('中国钢材价格网','')
                pz = (ulist[i][0] if (ulist[i][0] is None) else ulist[i][0].strip())
                cz = (ulist[i][1] if (ulist[i][1] is None) else ulist[i][1].strip())
                gg = (ulist[i][2] if (ulist[i][2] is None) else ulist[i][2].strip())
                jg = (ulist[i][3] if (ulist[i][3] is None) else ulist[i][3].strip())
                zd = (ulist[i][4] if (ulist[i][4] is None) else ulist[i][4].strip())
                gc = (ulist[i][5] if (ulist[i][5] is None) else ulist[i][5].strip())
                bz = (ulist[i][6] if (ulist[i][6] is None) else ulist[i][6].strip())
                print(title,sj,pz, cz, gg, jg, zd, gc, bz)

                db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='china_gcw')
                cursor = db.cursor()

                insert_color = (
                "INSERT INTO gcjgw_hb(title,sj,pz,cz,gg,jg,zd,gc,bz)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                data_color = (title,sj,pz, cz, gg, jg, zd, gc, bz)
                cursor.execute(insert_color, data_color)
                db.commit()
                cursor.close()
                db.close()
            except:
                continue

    except:
        print("不存在")
        trs = soup.select(".content-text1 table tbody tr")
        ulist = []
        for tr in range(1, len(trs)):
            ui = []
            for td in trs[tr]:
                ui.append(td.string)
            ulist.append(ui)
        for i in range(len(ulist)):
            try:
                title = driver.find_element_by_id('content-title').text
                sj = (driver.find_element_by_id('content-copyright').text).replace('www.zh818.com','').replace('中国钢材价格网','')
                pz = (ulist[i][1] if (ulist[i][1] is None) else ulist[i][1].strip())
                cz = (ulist[i][2] if (ulist[i][2] is None) else ulist[i][2].strip())
                gg = (ulist[i][3] if (ulist[i][3] is None) else ulist[i][3].strip())
                jg = (ulist[i][4] if (ulist[i][4] is None) else ulist[i][4].strip())
                zd = (ulist[i][5] if (ulist[i][5] is None) else ulist[i][5].strip())
                gc = (ulist[i][6] if (ulist[i][6] is None) else ulist[i][6].strip())
                bz = (ulist[i][7] if (ulist[i][7] is None) else ulist[i][7].strip())
                print(title,sj,pz, cz, gg, jg, zd, gc, bz)
                db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='china_gcw')
                cursor = db.cursor()
                insert_color = (
                    "INSERT INTO gcjgw_hb(title,sj,pz,cz,gg,jg,zd,gc,bz)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                data_color = (title, sj, pz, cz, gg, jg, zd, gc, bz)
                cursor.execute(insert_color, data_color)
                db.commit()
                cursor.close()
                db.close()
            except:
                continue

    l+=1
    driver.close()
    driver.switch_to.window(handles[0])
    main(jsonData, l)



if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='china_gcw')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT id,url FROM gcw_url_bd"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果

    for row in results:
        result = {}
        result_ = row[1]
        jsonData.append(result_)
    main(jsonData,l)
    print(len(results))
    db.close()

