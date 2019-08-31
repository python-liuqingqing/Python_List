import mysql.connector
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pyquery import PyQuery as pq
l=1;
driver = webdriver.Chrome()  # 打开火狐浏览器
driver.get('http://www.hbczfdc.com:4993/HPMS/QueryRoomList.aspx')
driver.find_element_by_id('PageNavigator1_txtNewPageIndex').clear()

def page_fy(l):
    print(l)
    if(l==8558):
        driver.close()
    driver.find_element_by_id('PageNavigator1_txtNewPageIndex').send_keys(l)
    driver.find_element_by_id('PageNavigator1_LnkBtnGoto').click()
    driver.find_element_by_id('PageNavigator1_txtNewPageIndex').clear()
    html = driver.page_source
    d = pq(html)
    len_=d(".resultlist2>table>tbody>tr")
    for i in range(1,len(len_)):
        # 开发公司	项目名称	面积(㎡)	单价(元)	楼层	单元名	户型	房屋地址	预售许可证号	状态
        kfgs = len_.eq(i).children('td').eq(1).text()
        xmmc  = len_.eq(i).children('td').eq(2).text()
        mj  = len_.eq(i).children('td').eq(3).text()
        dj  = len_.eq(i).children('td').eq(4).text()
        lc = len_.eq(i).children('td').eq(5).text()
        dym = len_.eq(i).children('td').eq(6).text()
        hx = len_.eq(i).children('td').eq(7).text()
        fwdz = len_.eq(i).children('td').eq(8).text()
        fwdz_href = len_.eq(i).children('td').eq(8).children('a').attr('href')
        ysxkz = len_.eq(i).children('td').eq(9).text()
        zt = len_.eq(i).children('td').eq(10).text()

        myobj={
            "kfgs":kfgs,
            "xmmc":xmmc,
            "mj":mj,
            "dj":dj,
            "lc":lc,
            "dym":dym,
            "hx":hx,
            "fwdz":fwdz,
            "fwdz_href":fwdz_href,
            "ysxkz":ysxkz,
            "zt":zt
        }
        print(myobj)
        import pymongo

        myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        mydb = myclient["cz_data"]
        mycol = mydb["cz_wqysws"]
        x = mycol.insert_one(myobj)

    #     db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='cz_data')
    #     cursor = db.cursor()
    #
    #     insert_color = (
    #         "INSERT INTO cz_wqspf_a(xmmc,xmwz,xkzh,kfqy,zh,xmdz,pq_time)" "VALUES(%s,%s,%s,%s,%s,%s,%s)")
    #     data_color = (xmmc,xmwz,xkzh,kfqy,zh,xmdz,
    #                   time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    #     cursor.execute(insert_color, data_color)
    #     db.commit()
    #     db.close()
    #     print(myobj)
    l=l+1
    page_fy(l)


if __name__ == '__main__':
    page_fy(l)
