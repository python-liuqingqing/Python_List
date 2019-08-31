# -*- coding:utf-8 -*-
import mysql.connector
import time
import  string
import math
from urllib.parse import quote
from bs4 import BeautifulSoup
from openpyxl import workbook  # 写入Excel表所用
from selenium import webdriver


l=0
jsonData1 = []
jsonData2 = []
jsonData3 = []
driver = webdriver.Firefox()  # 打开火狐浏览器
# 18264822355
driver.get('https://www.qichacha.com/user_login')
time.sleep(30)
def main(jsonData1,jsonData2,jsonData3,l):
    url=quote(jsonData2[l],safe = string.printable)
    print(url)
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("' + str(url) + '");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)
    time.sleep(2)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'lxml')
    trs = soup.select("table tbody tr")
    ulist = []
    for tr in range(len(trs)):
        ui = []
        for td in trs[tr]:
            ui.append(td)
        ulist.append(ui)
    for i in range(1,len(ulist)):

        xh = ulist[i][1].text

        ajmc = ulist[i][3].text

        ajmc_m = ulist[i][3].a['href']

        fbsj = ulist[i][5].text

        ajbh = ulist[i][7].text

        ajsf = ulist[i][9].text

        zxfy = ulist[i][11].text
        a=str(jsonData3[l])
        a.encode()
        print(xh,ajmc,ajmc_m,fbsj,ajbh,ajsf,zxfy)
    #
    driver.close()
    driver.switch_to_window(handles[0])
    time.sleep(2)
    l += 1
    main(jsonData1, jsonData2, jsonData3, l)

if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='qichacha_12',use_unicode=True, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "select id_a,url,gsmc from cpws_url"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    # 打印结果
    for row in results:
        result1 = {}
        result1 = row[0]
        result2 = {}
        result2 = row[1]
        result3 = {}
        result3 = row[2]
        jsonData1.append(result1)
        jsonData2.append(result2)
        jsonData3.append(result3)
    main(jsonData1, jsonData2, jsonData3, l)
    print(len(results))
    # except:
    #     print("数据库错误")

    # 关闭数据库连接
    db.close()