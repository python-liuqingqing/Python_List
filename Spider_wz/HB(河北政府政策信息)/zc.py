#coding:utf-8
import requests
import urllib
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium import webdriver
import os
# import sys
# sys.setrecursionlimit(10000)

jsonData1=[]
jsonData2=[]
jsonData3=[]
l=0

def main(jsonData1,jsonData2,jsonData3,l):
    print(l)
    print(jsonData1[l],jsonData2[l],jsonData3[l])
    headers = {

        }
    r = requests.get(jsonData1[l],headers=headers)
    # print(r.text)
    isExists = os.path.exists(os.getcwd()+'/'+jsonData3[l])
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(os.getcwd()+'/'+jsonData3[l])

    # # 状态码
    fp = open(os.getcwd()+'/'+jsonData3[l]+'/{}.doc'.format(jsonData2[l].replace('/','')), 'wb')
    fp.write(r.content)
    fp.close()
    # time.sleep(1)
    l+=1
    main(jsonData1, jsonData2, jsonData3, l)

if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='master')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT url,name,type FROM baidu_"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果

    for row in results:
        url_a = row[0].decode('utf-8')
        # print(url_a)
        name_a = row[1].decode('utf-8')
        # print(name_a)
        url_a_ = row[2].decode('utf-8')
        # print(url_a_)
        jsonData1.append(url_a)
        jsonData2.append(name_a)
        jsonData3.append(url_a_)
    main(jsonData1,jsonData2,jsonData3,l)
    print(len(results))
    db.close()