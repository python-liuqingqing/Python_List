# coding:utf-8
import mysql.connector
import time
import urllib
import re
from PIL import Image
from aip import AipOcr
from os import path
from bs4 import BeautifulSoup
from openpyxl import workbook  # 写入Excel表所用
from selenium import webdriver

l=1440
jsonData = []
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('http://www.gldjc.com/login?hostUrl=http%3A%2F%2Fwww.gldjc.com%2F')
driver.find_element_by_id('userName').send_keys('vip1712210204')
driver.find_element_by_id('password').send_keys('xtrj9900')
driver.find_element_by_id('loginBtn').click()

def python_baidu():
    picfile = 'D:/YZM/1.jpg'
    filename = path.basename(picfile)

    APP_ID = '10710735'  # 刚才获取的 ID，下同
    API_KEY = '42XxnGaFENV4rcWk1dFiulDZ'
    SECRECT_KEY = 'vNN9W604gIFTu4tDZ6vhxVZrzo0aPWOO'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    # message = client.basicAccurate(img)   # 通用文字高精度识别，每天 800 次免费
    for line in message["words_result"]:
        print(line["words"])
        return line["words"]

punctuation = '/!,;：:?"\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip().lower()

def main(jsonData,l):
    print(l)
    print(jsonData[l])
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("' + str(jsonData[l]) + '");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)
    time.sleep(3)
    # driver.refresh()
    driver.execute_script(""" 
                (function () { 
                    var y = document.body.scrollTop; 
                    var step = 100; 
                    window.scroll(0, y); 
                    function f() { 
                        if (y < document.body.scrollHeight) { 
                            y += step; 
                            window.scroll(0, y); 
                            setTimeout(f, 50); 
                        }
                        else { 
                            window.scroll(0, y); 
                            document.title += "scroll-done"; 
                        } 
                    } 
                    setTimeout(f, 1000); 
                })(); 
                """)
    time.sleep(2)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'lxml')
    title = soup.find(attrs={'class': 'highcharts-title'}).text
    title1 = soup.find(attrs={'class': 'highcharts-subtitle'}).text
    # print(title)
    # com_names = soup.find_all(class_='data_table')

    wb = workbook.Workbook()  # 创建Excel对象
    ws = wb.active  # 获取当前正在操作的表对象
    # 往表中写入标题行,以列表形式写入！
    ws.append([title])
    ws.append([title1])
    ws.append(['序号', '名称', '规格型号', '单位', '税率', '除税价(元)', '含税价(元)', '日期', '备注'])

    trs = soup.select("#infoprice_table tr")
    ulist = []
    for tr in range(1, len(trs)):
        ui = []
        for td in trs[tr]:
            ui.append(td)
        ulist.append(ui)
    for i in range(len(ulist)):
        xh = ulist[i][0].text
        mc = ulist[i][1].text
        ggxh = ulist[i][2].text
        dw = ulist[i][3].text
        sl = ulist[i][4].text
        csj = ulist[i][5].text
        result = ulist[i][6].img['src']
        urllib.request.urlretrieve(result, 'D:/YZM/1.jpg')
        image = Image.open('D:/YZM/1.jpg')
        # hsj = tesserocr.image_to_text(image)

        # fl = open('D:/YZM/1.jpg', 'rb')
        # image = Image.open(fl)
        # image.show()
        # # image.load()
        # hsj = pytesseract.image_to_string(image)
        # print(hsj)
        rq = ulist[i][7].text
        bz = ulist[i][8].text
        ws.append(
            [xh, mc, ggxh, dw, sl, csj, python_baidu(), rq, bz])
    print(str(l)+"-"+ removePunctuation(title).replace(' ', '') + '.xlsx')
    wb.save(str(l)+"-"+ removePunctuation(title).replace(' ', '')+'.xlsx')
    driver.close()
    driver.switch_to_window(handles[0])
    time.sleep(2)
    l+=1
    main(jsonData, l)

if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='gcw')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT url FROM gcw_url where TIME = 2015 "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 打印结果
        for row in results:
            result = {}
            result = row[0]
            jsonData.append(result)
        main(jsonData, l)
        print(len(results))
    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()
