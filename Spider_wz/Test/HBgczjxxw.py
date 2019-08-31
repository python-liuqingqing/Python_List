# coding=utf-8
import time
import mysql.connector
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pyquery import PyQuery as pq
import datetime

driver = webdriver.Chrome()  # 打开火狐浏览器
driver.get('http://110.249.221.15/ShowMMPrice.aspx')  # 打开界面
def ff():
    js = 'window.open("http://110.249.221.15/ShowMMPrice.aspx");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(3)
    city_id = ['1304'] #['1301','1302','1303','1304','1305','1306','1307','1308','1309','1310','1311']
    for v in range(len(city_id)):
        print(city_id[v])
    # 进行城市的切换
        s = driver.find_element_by_xpath('//*[@id="ddlCity"]')
        s.find_element_by_xpath('//option[@value="'+city_id[v]+'"]').click()
        time.sleep(3)
        for i in range(12, 45):
            # ++++++++++++++++++++++++++++++++++++++++
            if (i>=45):
                h = 15
            else:
                h = 14

            print("==================={}======={}=====".format(i,h))
            Select(driver.find_element_by_id("ddlQks")).select_by_index(i)
            year = driver.execute_script('return $("#ddlQks option:checked").text();')
            time.sleep(1)
            for y in range(1, h):
                time.sleep(1)
                print("===================={}".format(y))
                try:
                    if(y>= 12):
                        if(i>=45):
                            y = y-2
                        else:
                            y = y-1
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id="gvInfo"]/tbody/tr[27]/td/table/tbody/tr/td[' + str(y) + ']/a').click()
                    except:
                        # ++++++++++++++++++++++++++++++++++++++++
                        if(i> 12):
                            try:
                                driver.find_element_by_xpath('//*[@id="gvInfo"]/tbody/tr[7]/td/table/tbody/tr/td[1]/a').click()
                            except:
                                driver.find_element_by_xpath('//*[@id="gvInfo"]/tbody/tr[9]/td/table/tbody/tr/td[1]/a').click()
                        print("报错！！！")
                    html = driver.execute_script("return document.documentElement.outerHTML")
                    res = pq(html)
                    t_count = res('#gvInfo').children('tbody').children('tr')

                    for t in range(1, len(t_count) - 1):

                        bh = t_count.eq(t).children('td').eq(0).text()
                        # 材料名称规格
                        name_mc = t_count.eq(t).children('td').eq(1).text()
                        # 单位
                        dw = t_count.eq(t).children('td').eq(2).text()
                        # 价格
                        price = t_count.eq(t).children('td').eq(3).text()

                        print(city_id[v],year, bh, name_mc, dw, price)

                        # db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='hbgczjxx')
                        # cursor = db.cursor()
                        #
                        # insert_color = (
                        #     "INSERT INTO jg(city,year, bh, name_mc, dw, price)" "VALUES(%s,%s,%s,%s,%s,%s)")
                        # data_color = ('石家庄', year, bh, name_mc, dw, price)
                        # cursor.execute(insert_color, data_color)
                        # db.commit()
                        # cursor.close()
                        # db.close()
                except:
                    continue
    #
    #
    # # driver.close()
    # # driver.switch_to.window(handles[0])

if __name__ == '__main__':
    ff()