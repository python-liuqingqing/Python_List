# coding=utf-8
import time
import datetime
import mysql.connector
import re
import redis
from bs4 import BeautifulSoup
from selenium import webdriver
import landchina.ss_city
import requests
import time
driver = webdriver.Chrome()  # 打开火狐浏览器
driver.get('http://www.landchina.com/default.aspx?tabid=264&ComName=default')  # 打开界面
i = 1
l = 0
date_list = []
time.sleep(3)
start = '2016-1-1'
end = '2019-7-1'

def page_zh(i,l,key,zd,handles):
    # 获取本时间段内的总页数（方法）int(reg[0])
    zys = driver.find_elements_by_css_selector(".pager")
    try:
        str = zys[7].text
        print(str)
        reg = re.findall(r'\d+', str)
        print(reg)
        pages = int(reg[0])
        print("总页数为:" + reg[0])
        tds = driver.find_element_by_xpath(
            '//*[@id="mainModuleContainer_492_1114_495_1577_862_tdExtendProContainer"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/input[1]')
        # # 清空文本方法
        tds.clear()
        tds.send_keys(i)
        print("第" + tds.get_attribute("value") + "页")
        driver.find_element_by_xpath(
            '//*[@id="mainModuleContainer_492_1114_495_1577_862_tdExtendProContainer"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/input[2]').click()
    except:
        pages = 1

    time.sleep(2)
    # 获取页面html
    try:
        html = driver.find_element_by_id('top3_contentTable').get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
        href_ = soup.select('.queryCellBordy a')
        for line in href_:
            print("http://www.landchina.com/" + line['href'])
            db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='master')
            cursor = db.cursor()
            insert_color = (
                "INSERT INTO landchina (url,city,bh)" "VALUES(%s,%s,%s)")
            url = "http://www.landchina.com/" + line['href']
            data_color = (url, zd, key)
            cursor.execute(insert_color, data_color)
            db.commit()
            print('成功插入', cursor.rowcount, '条数据')
            # 关闭连接
            cursor.close()
            db.close()
        if (i < pages):
            i = i + 1
            page_zh(i, l, key, zd, handles)
        else:
            print("本次采集结束!!!")
            driver.close()
            driver.switch_to.window(handles[0])
    except:
        print(i,l,key,zd)
        driver.close()
        driver.switch_to_window(handles[0])
        llq_main(key, zd)



def llq_main(key,zd):
    print(start,end)
    try:
        js = 'window.open("http://www.landchina.com/default.aspx?tabid=264&ComName=default");'
        driver.execute_script(js)
        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        for handle in handles:  # 切换窗口（切换到搜狗）
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
        time.sleep(2)

        driver.find_element_by_id('mainModuleContainer_492_1114_495_TabMenu1_TabItem3').click()

        # 进行行政区的选择
        driver.find_element_by_id('top3_QueryConditionItem81').click()
        driver.execute_script("document.getElementById('top3_queryTblEnumItem_81_v').setAttribute('type', 'text');")
        driver.find_element_by_id('top3_queryTblEnumItem_81_v').clear()
        driver.find_element_by_id('top3_queryTblEnumItem_81_v').send_keys(key)

        # 对时间条件进行赋值
        driver.find_element_by_id('top3_QueryConditionItem291').click()
        driver.find_element_by_id('top3_queryDateItem_291_1').clear()
        driver.find_element_by_id('top3_queryDateItem_291_1').send_keys(start)
        driver.find_element_by_id('top3_queryDateItem_291_2').clear()
        driver.find_element_by_id('top3_queryDateItem_291_2').send_keys(end)

        driver.find_element_by_id('top3_QueryButtonControl').click()  # 查询操作
        page_zh(i,l,key,zd,handles)
    except:
        driver.close()
        driver.switch_to_window(handles[0])
        llq_main(key, zd)

if __name__ == '__main__':
    city_=landchina.ss_city.zd
    for key in city_:
        zd = city_[key]
        # print(zd1)
        print(key,zd)
        llq_main(key,zd)