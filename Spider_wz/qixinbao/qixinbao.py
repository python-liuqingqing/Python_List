# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
import threading
from selenium import webdriver
driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get("http://www.qixin.com/auth/login?return_url=%2F")  # 打开界面
driver.find_element_by_css_selector(".input-flat-user").send_keys("13181818509")
driver.find_element_by_css_selector(".input-flat-lock").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div/div/div[2]/div/span/input[2]").send_keys("泰安光彩大市场")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div/div/div[2]/div/i").click()
driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[4]/div/div/div/input").send_keys(431)
driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[4]/div/div/div/button").click()
i=431
def main(i):
    # 获取页面html
    file = open('D:\GC\labels'+str(i)+'.txt', 'w')
    file.close()
    html = driver.page_source
    fos = open('D:\GC\labels'+str(i)+'.txt', "w", encoding="utf-8")
    fos.write(html)
    fos.close()
    i=i+1
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[4]/div/div/div/input").clear()
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[4]/div/div/div/input").send_keys(i)
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[4]/div/div/div/button").click()
    if(1%16==0):
        time.sleep(30)
        main(i)
    else:
        main(i)


main(i)

