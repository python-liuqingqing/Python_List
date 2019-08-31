# coding:utf-8
import mysql.connector
import time
from bs4 import BeautifulSoup
from selenium import webdriver

l=153 #1 34
jsonData=[]
json_city=[]

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
def main(jsonData, l):
    print(jsonData[l].decode(),str(l))
    # 新开一个窗口，通过执行js来新开一个窗口
    print(jsonData[l].decode())
    js = 'window.open("'+(jsonData[l].decode()).replace('https:','https://')+'");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/ul/li[2]/a').click()
    time.sleep(2)

    lpqh =driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[1]/a[3]').text
    # 楼盘名称
    lpmc =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/div[2]/a').text
    #楼盘特点
    lptd =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div[2]').text
    #参考单价
    ckdj =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/div[2]').text
    #物业类型
    wylx =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[4]/div[2]').text
    #开发商
    kfs =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[5]/div[2]/a').text
    #区域位置
    qywz =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[6]/div[2]').text
    #楼盘地址
    lpdz =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[7]/div[2]').text
    #售楼处电话
    slcdh =""#driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[8]/div[2]').text
    #最低首付
    zdsf =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div[2]/ul/li[1]/div[2]').text
    #楼盘户型
    lphx =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div[2]/ul/li[2]/div[2]').text
    #最新开盘
    zxkp =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div[2]/ul/li[3]/div[2]').text
    #交房时间
    jfsj =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div[2]/ul/li[4]/div[2]').text
    #售楼处地址
    slcdz =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div[2]/ul/li[5]/div[2]').text
    try:
        # 建筑类型
        jzlx = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[1]/div[2]').text
        # 产权年限
        cqnx = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[2]/div[2]').text
        # 绿化率
        lhl = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[3]/div[2]').text
        # 规划户数
        ghhs = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[5]/div[2]').text
        # 楼层状况
        lczk = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[5]/div[2]').text
        # 物业管理费
        wyglf = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[6]/div[2]').text
        # 物业公司
        wygs = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[6]/div[2]').text
    except:
        # 建筑类型
        jzlx = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[1]/div[2]').text
        # 产权年限
        cqnx =""
        # 绿化率
        lhl =""
        # 规划户数
        ghhs =""
        # 楼层状况
        lczk =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[2]/div[2]').text
        # 物业管理费
        wyglf =driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[3]/div[2]').text
        # 物业公司
        try:
            wygs = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li[4]/div[2]').text
        except:
            wygs=""


    data={
        "url":(jsonData[l].decode()).replace('https:','https://'),
        "lpqh":lpqh,
        # 楼盘名称
        "lpmc":lpmc,
        # 楼盘特点
         "lptd":lptd,
        # 参考单价
        "ckdj":ckdj.replace('[价格走势]',''),
        # 物业类型
         "wylx":wylx,
        # 开发商
         "kfs":kfs,
        # 区域位置
         "qywz":qywz,
        # 楼盘地址
         "lpdz":lpdz.replace('[查看地图]',''),
        # 售楼处电话
         "slcdh":slcdh,
        # 最低首付
         "zdsf":zdsf.replace('[房贷计算器]',''),
        # 楼盘户型
         "lphx":lphx,
        # 最新开盘
         "zxkp":zxkp,
        # 交房时间
         "jfsj":jfsj,
        # 售楼处地址
         "slcdz":slcdz,
        # 建筑类型
         "jzlx":jzlx.replace('[查看详情]',''),
        # 产权年限
         "cqnx":cqnx.replace('[查看详情]',''),
        # 绿化率
         "lhl":lhl.replace('[查看详情]',''),
        # 规划户数
         "ghhs":ghhs,
        # 楼层状况
         "lczk":lczk,
        # 物业管理费
         "wyglf":wyglf,
        # 物业公司
         "wygs":wygs
    }

    print(data)
    import pymongo

    myclient = pymongo.MongoClient("mongodb://192.168.1.19:27017/")
    mydb = myclient["ajk"]
    mycol = mydb["ajk_lpxq_dz"]
    mydict = data
    x = mycol.insert_one(mydict)
    driver.close()
    driver.switch_to_window(handles[0])
    l += 1
    main(jsonData, l)




if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='master')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT url FROM ajk_href_dz"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果
    for row in results:
        result = {}
        city_list = {}
        result = row[0]
        jsonData.append(result)
    main(jsonData,l)
    print(len(results))
    # try:

    # except:
    #     print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()