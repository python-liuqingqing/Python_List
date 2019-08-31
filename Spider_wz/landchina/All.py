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

url_tid = "http://www.superfastip.com/api/ip?tid=55d9bb0c8648afa7841e81a4cb4f77da&type=0"
res = requests.get(url_tid)
proxy = {"http": "http://proxy.superfastip.com:7798",
        "https": "http://proxy.superfastip.com:7798"}

driver = webdriver.Chrome()  # 打开火狐浏览器

# chromeOptions = webdriver.ChromeOptions()
# # 设置代理
# chromeOptions.add_argument("--proxy-server=http://proxy.superfastip.com:7798")
# # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
# driver = webdriver.Chrome(chrome_options = chromeOptions)

driver.get('http://www.landchina.com/default.aspx?tabid=263&ComName=default')  # 打开界面
i = 1
l = 0
start = '2019-7-1'
end = '2019-17-31'
date_list = []
time.sleep(3)

def page_zh(i,l,key,zd,handles):
    # 获取本时间段内的总页数（方法）int(reg[0])
    zys = driver.find_elements_by_css_selector(".pager")
    if(zys!=[]):
        str = zys[1].text
        reg = re.findall(r'\d+', str)
        pages = int(reg[0])
        print("总页数为:" + reg[0])
        tds = driver.find_elements_by_css_selector(".pager>input")
        # 清空文本方法
        tds[0].clear()
        tds[0].send_keys(i)
        print("第" + tds[0].get_attribute("value") + "页")
        tds[1].click()
    elif(zys==[]):
        pages=1

    time.sleep(2)
    # 获取页面html
    try:
        html = driver.find_element_by_id('TAB_contentTable').get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
        href_ = soup.select('.queryCellBordy a')
        for line in href_:
            print("http://www.landchina.com/" + line['href'])
            # db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='master')
            # cursor = db.cursor()
            #
            # insert_color = (
            #     "INSERT INTO landchina_ta (url,city,bh)" "VALUES(%s,%s,%s)")
            # url = "http://www.landchina.com/" + line['href']
            # data_color = (url, zd, key)
            # cursor.execute(insert_color, data_color)
            # db.commit()
            # print('成功插入', cursor.rowcount, '条数据')
            # # 关闭连接
            # cursor.close()
            # db.close()

        if (i < pages):
            i = i + 1
            page_zh(i, l,key,zd,handles)
        else:
            print("本次采集结束!!!")
            driver.close()
            driver.switch_to_window(handles[0])
    except:
        print(i,l,key,zd)
        driver.close()
        driver.switch_to_window(handles[0])
        llq_main(key, zd)
# 关闭浏览器（selenium）
# driver.quit()
#
def llq_main(key,zd):
    print(start,end)
    js = 'window.open("http://www.landchina.com/default.aspx?tabid=263&ComName=default");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)
    time.sleep(2)
    driver.find_element_by_id('TAB_QueryConditionItem270').click()
    # 对时间条件进行赋值
    driver.find_element_by_id('TAB_queryDateItem_270_1').clear()
    driver.find_element_by_id('TAB_queryDateItem_270_1').send_keys(start)
    driver.find_element_by_id('TAB_queryDateItem_270_2').clear()
    driver.find_element_by_id('TAB_queryDateItem_270_2').send_keys(end)
    # 进行行政区的选择
    driver.find_element_by_id('TAB_QueryConditionItem256').click()
    driver.execute_script("document.getElementById('TAB_queryTblEnumItem_256_v').setAttribute('type', 'text');")
    driver.find_element_by_id('TAB_queryTblEnumItem_256_v').clear()
    driver.find_element_by_id('TAB_queryTblEnumItem_256_v').send_keys(key)
    driver.find_element_by_id('TAB_QueryButtonControl').click()  # 查询操作

    page_zh(i,l,key,zd,handles)


if __name__ == '__main__':
    # start = '2009-11-12'
    # end = '2018-09-18'
    # begin_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    # end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    # while begin_date <= end_date:
    #     date_str = begin_date.strftime("%Y-%m-%d")
    #     date_list.append(date_str)
    #     begin_date += datetime.timedelta(days=1)
    # for l in range(len(date_list)):
    #     # print(date_list[l])
    #     llq_main(date_list[l],date_list[l])



    # city_=landchina.ss_city.zd
    # for key in city_:
    #     zd = city_[key]
    #     print(key,zd)
    #     llq_main(key,zd)
    llq_main('370900', '泰安市本级')
