# coding:utf-8
import mysql.connector
import time
import math
from bs4 import BeautifulSoup
from openpyxl import workbook  # 写入Excel表所用
from selenium import webdriver

l=546
jsonData1 = []
jsonData2 = []
jsonData3 = []
driver = webdriver.Firefox()  # 打开火狐浏览器
# 18264822355
driver.get('https://www.qichacha.com/user_login')
time.sleep(30)
def main(jsonData1,jsonData2,jsonData3,l):
    print(l)
    print(jsonData1[l])
    url='https://www.qichacha.com/company_getinfos?unique=' + str(jsonData2[l]).replace('http://www.qichacha.com/firm_', '').replace(
            '.html', '') + '&companyname=' + str(jsonData3[l]).strip() + '&p=' + str(1) + '&&tab=susong&box=wenshu&casetype='
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
    try:
        title_num = soup.find(attrs={'class': 'tbadger'}).text
        if(int(title_num)>0):
            for d in range(math.ceil(int(title_num)/10)):
                dz = 'https://www.qichacha.com/company_getinfos?unique=' + str(jsonData2[l]).replace('http://www.qichacha.com/firm_', '').replace(
                '.html', '') + '&companyname=' + str(jsonData3[l]).strip() + '&p=' + str(d+1) + '&&tab=susong&box=wenshu&casetype='
                print(dz)

                connect = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='qichacha_12')
                # 获取游标
                cursor = connect.cursor()
                # 插入数据
                sql = "INSERT INTO  cpws_url(id_a,gsmc,url) VALUES ( '%s', '%s', '%s' )"
                data =(jsonData1[l],jsonData3[l],dz)
                cursor.execute(sql % data)
                connect.commit()
                print('成功插入', cursor.rowcount, '条数据')
                # 关闭连接
                cursor.close()
                connect.close()
    except:
        print('错误')
    driver.close()
    driver.switch_to_window(handles[0])
    time.sleep(2)
    l += 1
    main(jsonData1, jsonData2, jsonData3, l)

if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='qichacha_12')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "select id,url,gsmc from qichacha_main GROUP BY gsmc"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
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