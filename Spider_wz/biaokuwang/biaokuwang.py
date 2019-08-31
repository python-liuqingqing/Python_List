# coding=utf-8
from bs4 import BeautifulSoup
import mysql.connector
#
# path = 'D:/标库网/1 - 副本 (1).html'
#
# with open(path, 'r',encoding='gbk',errors='ignore') as f:
#     Soup = BeautifulSoup(f.read(), 'lxml')
#     titles = Soup.select('.pic>a')
#
# for title in titles:
#     print(title['href'])
for i in range(1,75):
    lj='D:/标库网/1 - 副本 ('+str(i)+').html'
    htmlf = open(lj, 'r', encoding="utf-8")
    htmlcont = htmlf.read()
    Soup = BeautifulSoup(htmlcont, 'lxml')
    titles = Soup.select('ul li .pic a')
    for title in titles:
        print("http://www.tmkoo.com"+title['href'])
        # # # 连接数据库
        connect = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='qichacha')
        # 获取游标
        cursor = connect.cursor()
        # 插入数据
        sql = "INSERT INTO  biaokuwang(url) VALUES ( '%s')"
        data = "http://www.tmkoo.com"+title['href']
        cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        # 关闭连接
        cursor.close()
        connect.close()