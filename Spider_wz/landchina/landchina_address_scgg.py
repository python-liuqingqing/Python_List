# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('http://www.landchina.com/default.aspx?tabid=263&ComName=default')  # 打开界面
# 对时间条件进行赋值
driver.find_element_by_id('TAB_QueryConditionItem270').click()
driver.find_element_by_id('TAB_queryDateItem_270_1').send_keys('2018-6-11')
driver.find_element_by_id('TAB_queryDateItem_270_2').send_keys('2018-6-19')
# 进行行政区的选择
# driver.find_element_by_id('TAB_QueryConditionItem256').click()
# driver.execute_script("document.getElementById('TAB_queryTblEnumItem_256_v').setAttribute('type', 'text');")
# driver.find_element_by_id('TAB_queryTblEnumItem_256_v').send_keys('13')
# 浏览器加载需要时间
time.sleep(2)
driver.find_element_by_id('TAB_QueryButtonControl').click()  # 查询操作
i=1;
#获取本时间段内的总页数（方法）int(reg[0])
zys=driver.find_elements_by_css_selector(".pager")
str=zys[1].text;
reg=re.findall(r'\d+', str)
pages=int(reg[0])
print("总页数为:"+reg[0])

def page_zh(i):
    tds = driver.find_elements_by_css_selector(".pager>input")
    # 清空文本方法
    tds[0].clear()
    tds[0].send_keys(i)
    print("第" + tds[0].get_attribute("value") + "页")
    tds[1].click()
    # 获取页面html
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
    href_ = soup.select('.queryCellBordy a')
    for line in href_:
        print("http://www.landchina.com/"+line['href'])
        # # # 连接数据库
        # connect = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='landchina')
        # # 获取游标
        # cursor = connect.cursor()
        # # 插入数据
        # sql = "INSERT INTO  landchina_jieguogg_url (url) VALUES ( '%s')"
        # data ="http://www.landchina.com/"+line['href']
        # cursor.execute(sql % data)
        # connect.commit()
        # print('成功插入', cursor.rowcount, '条数据')
        # # 关闭连接
        # cursor.close()
        # connect.close()
    if (i < pages):
        i=i+1
        page_zh(i)
    else:
        print("本次采集结束!!!")

page_zh(i)
# 关闭浏览器（selenium）
# driver.quit()

