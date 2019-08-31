import urllib.request
import pandas as pd
import requests
import mysql.connector
import time
import json
import random
# 将申请的key写入
jsonData=[]
json_xmmc=[]
l=0

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'guid=4dd2-2bc1-0908-7820; UM_distinctid=16c4c0dbed595b-094c5fb61b4ab1-1c3c6754-1fa400-16c4c0dbed6937; cna=aG/JFe5cBDwCAduSnDbHsy5L; _uab_collina=156464406647750809825234; key=bfe31f4e0fb231d29e1d3ce951e2c780; CNZZDATA1255626299=2018940098-1564641921-https%253A%252F%252Fwww.baidu.com%252F%7C1565333224; x5sec=7b22617365727665723b32223a223335373334663165333039363561613664636663616361643331346437666231434b3638744f6f46454b7131753575567350755652413d3d227d; isg=BJKSTR2PG2DmWmcTHrqpFBBJ4160C5f7kyTxUFzrlMUwbzJpRDMXTZaG34t2Hw7V; l=cBrAE0fHqYKZg2pxBOCNZuI8LzQtRIRAguPRwCDki_5IK1TsQsQOkWwDMe96cjWd9eLB40S5pSy9-etX9g2BomXJZb5P.',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

url_tid = "http://www.superfastip.com/api/ip?tid=150d1c8596f496761617ca9f8b86a6aa&type=0"
res = requests.get(url_tid)
proxy = {"http":"http://proxy.superfastip.com:7798",
        "https":"http://proxy.superfastip.com:7798"}

def main(jsonData,json_xmmc, l):
    try:
        print(jsonData[l], json_xmmc[l].decode(), str(l))
        address = '潍坊市奎文区{}'.format(json_xmmc[l].decode())
        # 获取小区边线
        requrl='https://ditu.amap.com/detail/get/detail?id={}'.format(json_xmmc[l].decode())
        # 获取小区周边
        # requrl = 'https://restapi.amap.com/v3/place/text?key=4b86820a7590de60e4f81f53e59ae17f&citylimit=true&output=json&keywords={}&city=潍坊'.format(address)
        # 获取小区位置的经纬度
        # requrl = 'http://restapi.amap.com/v3/geocode/geo?key=722d5d84a7fcc8da59b6c9b01f2f468d&s=rsv3&city=0536&address={}'.format(address)
        response = requests.get(requrl, headers=headers)#
        # data = response.json()
        # answer = response.json()
        # print(answer)
        # # print(answer['pois'][0])
        #
        # b_id = answer['pois'][0]['id']
        # b_name = answer['pois'][0]['name']
        # b_address = answer['pois'][0]['address']
        # if(b_address==[]):
        #     b_address=0
        #
        # b_location = answer['pois'][0]['location']

        # =====================解析获取边线的方式方法=====================
        data = json.loads(response.text)
        try:
            if data["status"] == "1":
                spec = data["data"]["spec"]
                border = spec["mining_shape"]["shape"]
                print("border ", border)
                # 连接数据库
                connect = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='dyq_tdjy')
                # 获取游标
                cursor = connect.cursor()
                # 插入数据
                sql = "update ajk_house set border = %s where id= %s"
                data = (border, jsonData[l])
                cursor.execute(sql, data)
                connect.commit()
                print('成功插入', cursor.rowcount, '条数据')
                # 关闭连接
                cursor.close()
                connect.close()
                time.sleep(random.randint(2, 6))
                l = l + 1
                main(jsonData, json_xmmc, l)
        #
        except:
            time.sleep(2)
            print("查询错误~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            l = l + 1
            main(jsonData, json_xmmc, l)

        # print(address + "的经纬度：", answer['geocodes'][0]['location'])
        # 连接数据库
        # connect = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='dyq_tdjy')
        # # 获取游标
        # cursor = connect.cursor()
        # # 插入数据
        # sql = "update ajk_house set b_id = %s,b_name= %s,b_address= %s, b_location= %s where id= %s"
        # data = (b_id, b_name, b_address, b_location, jsonData[l])
        # cursor.execute(sql, data)
        # connect.commit()
        # print('成功插入', cursor.rowcount, '条数据')
        # # 关闭连接
        # cursor.close()
        # connect.close()
        # #


    except:
        time.sleep(4)
        l = l + 1
        main(jsonData, json_xmmc, l)

if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='dyq_tdjy')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "select id,b_id from ajk_house where border is null "
    # sql = "select id,house from ajk_house where id>215"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果
    for row in results:
        result = {}
        xmmc_list = {}
        result = row[0]
        xmmc_list = row[1]
        jsonData.append(result)
        json_xmmc.append(xmmc_list)
    main(jsonData, json_xmmc, l)
    print(len(results))
    # try:

    # except:
    #     print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()