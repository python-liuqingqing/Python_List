import mysql.connector
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pyquery import PyQuery as pq
l=1;
driver = webdriver.Chrome()  # 打开火狐浏览器
driver.get('http://www.hbczfdc.com:4993/hpms/projectinfolist.aspx')
driver.find_element_by_id('PageNavigator1_txtNewPageIndex').clear()

def page_fy(l):
    print(l)
    if(l==108):
        driver.close()
    driver.find_element_by_id('PageNavigator1_txtNewPageIndex').send_keys(l)
    driver.find_element_by_id('PageNavigator1_LnkBtnGoto').click()
    driver.find_element_by_id('PageNavigator1_txtNewPageIndex').clear()
    html = driver.page_source
    d = pq(html)
    len_=d(".resultlist>table>tbody>tr")
    for i in range(1,len(len_)):
        xmmc = len_.eq(i).children('td').eq(1).text()
        #  项目网址
        xmwz = "http://www.hbczfdc.com:4993"+(len_.eq(i).children('td').eq(1).children('a').attr('href')).replace('..', '')
        #  许可证号
        xkzh = len_.eq(i).children('td').eq(2).text()
        #  开发企业
        kfqy = len_.eq(i).children('td').eq(3).text()
        #  幢号
        zh = len_.eq(i).children('td').eq(4).text()
        #  项目地址
        xmdz = len_.eq(i).children('td').eq(5).text()
        myobj = {
            "xmmc": xmmc,
            "xmwz": xmwz,
            "xkzh": xkzh,
            "kfqy": kfqy,
            "zh": zh,
            "xmdz": xmdz
        }
        db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='cz_data')
        cursor = db.cursor()

        insert_color = (
            "INSERT INTO cz_wqspf_a(xmmc,xmwz,xkzh,kfqy,zh,xmdz,pq_time)" "VALUES(%s,%s,%s,%s,%s,%s,%s)")
        data_color = (xmmc,xmwz,xkzh,kfqy,zh,xmdz,
                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        cursor.execute(insert_color, data_color)
        db.commit()
        db.close()
        print(myobj)
    l=l+1
    page_fy(l)


if __name__ == '__main__':
    page_fy(l)
