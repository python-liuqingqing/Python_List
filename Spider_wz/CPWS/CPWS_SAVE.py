# coding:utf-8
from selenium import webdriver
import time
import mysql.connector
i = 214
jsonData = []
jsonData_ = []

driver=webdriver.Firefox()
# driver=webdriver.PhantomJS(executable_path="C:\Python36\Scripts\phantomjs.exe")
driver.get("https://www.baidu.com/")

def main(jsonData,jsonData_,i):
    print(jsonData_[i])
    print(i)
    js = 'window.open("' + str(jsonData_[i]) + '");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)
    time.sleep(5)
    add_a = driver.find_element_by_id('Content').get_attribute("innerHTML")
    # 获取页面html

    add_b = driver.find_element_by_id('Content').text

    # 连接数据库
    connect = mysql.connector.connect(user='root', password='xtkm9900', host='192.168.1.130', database='caipanwenshu')
    # 获取游标
    cursor = connect.cursor()
    # 插入数据
    sql = "update cpws_china set add_a = %s,add_b = %s  where id="+str(jsonData[i])
    data = (add_a,add_b)
    cursor.execute(sql,data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')
    # 关闭连接
    cursor.close()
    connect.close()

    driver.close()
    driver.switch_to_window(handles[0])
    time.sleep(5)
    i+=1
    main(jsonData,jsonData_, i)

# 打开数据库连接
db = mysql.connector.connect(user='root', password='xtkm9900', host='192.168.1.130', database='caipanwenshu')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT id,wangzhi FROM cpws_china"
# try:
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
# 打印结果

for row in results:
    result = {}
    result = row[0]
    result_ = row[1].decode('utf-8')
    jsonData.append(result)
    jsonData_.append(result_)

main(jsonData, jsonData_, i)
print(len(results))
# except:
#    print("Error")

# 关闭数据库连接
db.close()
