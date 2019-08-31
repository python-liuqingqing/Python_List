#coding:utf-8
import requests
import urllib
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium import webdriver
import os
from lxml import etree
import sys
sys.setrecursionlimit(10000)

jsonData1=[]
jsonData2=[]
jsonData3=[]
l=0

def main(jsonData1,jsonData2,jsonData3,l):
    print(l)
    print(jsonData1[l],jsonData2[l],jsonData3[l])
    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_gscu_1603977019=58149402pk70ss13; _gscbrs_1603977019=1; _gscs_1603977019=58149402j22u5h13|pv:9',
            }
    url ='http://www.landvalue.com.cn/News/NewsRead?id={}'.format(jsonData2[l])
    # url= "http://www.landvalue.com.cn/News/NewsRead?id=0c2896fd26d348eeb51981ceb5a9ee92"
    print(url)
    r = requests.get(url,headers=headers)
    # 选取 ol/li/div[@class="item"] 不管它们在文档中的位置
    try:
        root = etree.HTML(r.content)
        items = "http://www.landvalue.com.cn{}".format(root.xpath('/html/body/div[2]/div/div[2]/div[2]/a/@href')[0])
        print(items)
        res = requests.get(items)
        res.encoding = res.apparent_encoding
        with open('{}.pdf'.format(jsonData3[l]), 'wb') as f:
            f.write(res.content)
            print("完成")
            l += 1
            main(jsonData1, jsonData2, jsonData3, l)
    except:
        fp = open(jsonData3[l]+'.doc', 'wb')
        fp.write(r.content)
        fp.close()
        print("完成+++")
        l += 1
        main(jsonData1, jsonData2, jsonData3, l)


    # print(r.text)
    # isExists = os.path.exists(os.getcwd()+'/'+jsonData3[l])
    # # 判断结果
    # if not isExists:
    #     # 如果不存在则创建目录
    #     # 创建目录操作函数
    #     os.makedirs(os.getcwd()+'/'+jsonData3[l])
    #
    # # # 状态码


if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='master')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM zgdj"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果

    for row in results:
        url_a = row[0]
        name_a = row[1].decode('utf-8')
        url_a_ = row[2].decode('utf-8')
        jsonData1.append(url_a)
        jsonData2.append(name_a)
        jsonData3.append(url_a_)
    main(jsonData1,jsonData2,jsonData3,l)
    print(len(results))
    db.close()