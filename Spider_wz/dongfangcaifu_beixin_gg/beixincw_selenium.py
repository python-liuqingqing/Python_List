# coding=utf-8
import time
import mysql.connector
import re
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://data.eastmoney.com/bbsj/201809/lrb.html')  # 打开界面
driver.find_element_by_id('PageContgopage').clear()
driver.find_element_by_id('PageContgopage').send_keys(2);
driver.find_element_by_xpath('//*[@id="PageCont"]/a[9]').click()
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')  # 对html进行解析
trs = soup.select("#dt_1 tbody tr")
ulist = []
for tr in range(len(trs)):
    ui = []
    for td in trs[tr]:
        ui.append(td)
    ulist.append(ui)
for i in range(len(ulist)):
    #股票代码
    gpdm = ulist[i][1].text
    #股票简称
    gpjc = ulist[i][2].text
    #相关
    xg= ulist[i][3].a['href']
    #净利润
    jlr= ulist[i][4].text
    #净利润同比
    jlrtb= ulist[i][5].text
    #营业总收入
    yyzsr= ulist[i][6].text
    #营业总收入同比
    yyzsrtb= ulist[i][7].text
    #营业支出
    yyzc= ulist[i][8].text
    #销售费用
    xsfy= ulist[i][9].text
    #管理费用
    glfy= ulist[i][10].text
    #财务费用
    cwfy= ulist[i][11].text
    #营业总支出
    yyzzc= ulist[i][12].text
    #营业利润
    yylr= ulist[i][13].text
    #利润总额
    lrze= ulist[i][14].text
    #公告日期
    ggrq= ulist[i][15].text

    data={
        # 股票代码
        "gpdm":gpdm,
        # 股票简称
        "gpjc":gpjc,
        # 相关
        "xg":xg,
        # 净利润
        "jlr":jlr,
        # 净利润同比
        "jlrtb":jlrtb,
        # 营业总收入
        "yyzsr":yyzsr,
        # 营业总收入同比
        "yyzsrtb":yyzsrtb,
        # 营业支出
        "yyzc":yyzc,
        # 销售费用
        "xsfy":xsfy,
        # 管理费用
        "glfy":glfy,
        # 财务费用
        "cwfy":cwfy,
        # 营业总支出
        "yyzzc":yyzzc,
        # 营业利润
        "yylr":yylr,
        # 利润总额
        "lrze":lrze,
        # 公告日期
        "ggrq":ggrq
    }
    print(data)


# driver.close()

