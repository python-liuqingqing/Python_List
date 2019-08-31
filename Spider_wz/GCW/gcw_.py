import requests
import urllib
from bs4 import BeautifulSoup
import pytesseract
import re
import tesserocr
from PIL import Image
import random
import time
import math
from openpyxl import workbook  # 写入Excel表所用
from aip import AipOcr
from os import path
import mysql.connector
from selenium import webdriver

def python_baidu():
    picfile = 'D:/YZM/1.jpg'
    filename = path.basename(picfile)

    APP_ID = '10710735'  # 刚才获取的 ID，下同
    API_KEY = '42XxnGaFENV4rcWk1dFiulDZ'
    SECRECT_KEY = 'vNN9W604gIFTu4tDZ6vhxVZrzo0aPWOO'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    # message = client.basicAccurate(img)   # 通用文字高精度识别，每天 800 次免费
    for line in message["words_result"]:
        print(line["words"])
        return line["words"]

def get_user_agent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0) ,Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Opera/9.25 (Windows NT 5.1; U; en), Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
        "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
        "Mozilla/2.02E (Win95; U)",
        "Mozilla/3.01Gold (Win95; I)",
        "Mozilla/4.8 [en] (Windows NT 5.1; U)",
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
        "HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
        "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
        "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
    ]
    uer_agent = random.choice(user_agent_list)
    return uer_agent

def headers():
    headers = {
        'Host': 'info.gldjc.com',
        'User-Agent': get_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie':  'location_name=%25E5%25B1%25B1%25E4%25B8%259C; location_code=370000; NTKF_T2D_CLIENTID=guest81A5E8B7-3986-6BB6-B61C-F4CC6ADE1843; _ga=GA1.2.544104654.1533115395; _gid=GA1.2.621484555.1533115395; Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6=1533115394,1533170515; Hm_lvt_727d5904b141f326c9cb1ede703d1162=1533115394,1533170515; INFO_PRICE_LOCATION=39_1; backUrlParameter=periodId%3D103185%26level%3D1%26p%3D2%26categoryId%3D191923%26locationId%3D39%26categoryLevel%3D1%26major%3D%25E5%2585%25A8%25E9%2583%25A8; gldjc_sessionid=2fb6b206-eb56-4ea8-be69-49b4c69d3982; _gat_gtag_UA_110560299_1=1; loginUuid=2fb6b206-eb56-4ea8-be69-49b4c69d3982; Hm_lpvt_727d5904b141f326c9cb1ede703d1162=1533284107; Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6=1533284107; nTalk_CACHE_DATA={uid:kf_9318_ISME9754_6349427345656906564,tid:1533284062313329}'}
    return headers

def w_url(href,driver,categoryId):
    time.sleep(3)
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("'+str(href)+'");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)
    time.sleep(3)
    # driver.refresh()
    driver.execute_script(""" 
            (function () { 
                var y = document.body.scrollTop; 
                var step = 100; 
                window.scroll(0, y); 
                function f() { 
                    if (y < document.body.scrollHeight) { 
                        y += step; 
                        window.scroll(0, y); 
                        setTimeout(f, 50); 
                    }
                    else { 
                        window.scroll(0, y); 
                        document.title += "scroll-done"; 
                    } 
                } 
                setTimeout(f, 1000); 
            })(); 
            """)
    time.sleep(2)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, 'lxml')
    title = soup.find(attrs={'class': 'highcharts-title'}).text
    title1 = soup.find(attrs={'class': 'highcharts-subtitle'}).text


    # print(title)
    # com_names = soup.find_all(class_='data_table')

    wb = workbook.Workbook()  # 创建Excel对象
    ws = wb.active  # 获取当前正在操作的表对象
    # 往表中写入标题行,以列表形式写入！
    ws.append([title])
    ws.append([title1])
    ws.append(['序号', '名称', '规格型号', '单位', '税率','除税价(元)','含税价(元)','日期', '备注'])

    trs = soup.select("#infoprice_table tr")
    ulist = []
    for tr in range(1, len(trs)):
        ui = []
        for td in trs[tr]:
            ui.append(td)
        ulist.append(ui)
    for i in range(len(ulist)):
        xh = ulist[i][0].text
        mc = ulist[i][1].text
        ggxh= ulist[i][2].text
        dw= ulist[i][3].text
        sl= ulist[i][4].text
        csj= ulist[i][5].text
        result= ulist[i][6].img['src']
        urllib.request.urlretrieve(result, 'D:/YZM/1.jpg')
        image = Image.open('D:/YZM/1.jpg')
        # hsj = tesserocr.image_to_text(image)

        # fl = open('D:/YZM/1.jpg', 'rb')
        # image = Image.open(fl)
        # image.show()
        # # image.load()
        # hsj = pytesseract.image_to_string(image)
        # print(hsj)
        rq= ulist[i][7].text
        bz= ulist[i][8].text
        print(python_baidu())
        ws.append(
            [xh,mc,ggxh,dw,sl,csj,python_baidu(),rq,bz])
    wb.save(str(categoryId)+title.replace(":","")+'.xlsx')
    driver.close()
    driver.switch_to_window(handles[0])
    time.sleep(2)

def run(i,categoryId,categoryLevel):
    # driver = webdriver.Firefox()  # 打开火狐浏览器
    # driver.get('http://www.gldjc.com/login?hostUrl=http%3A%2F%2Fwww.gldjc.com%2F')
    # driver.find_element_by_id('userName').send_keys('vip1712210204')
    # driver.find_element_by_id('password').send_keys('xtrj9900')
    # driver.find_element_by_id('loginBtn').click()
    print('------------------第'+str(i)+"页")
    from urllib.parse import quote
    import string
    url = r'http://info.gldjc.com/info_price/so.html?periodId=88517&level=1&p='+str(i)+'&categoryId='+str(categoryId)+'&locationId=39&categoryLevel='+str(categoryLevel)+'&major=全部'
    url = quote(url, safe=string.printable)  # safe表示可以忽略的字符
    print(url)
    response = requests.get(url, headers=headers())
    time.sleep(3)
    if response.status_code != 200:
        response.encoding = 'utf-8'
        print(response.status_code)
        print('ERROR')
    soup = BeautifulSoup(response.text, 'lxml')
    trs = soup.select(".info-list table tbody tr")
    ulist = []
    for tr in range(len(trs)):
        ui = []
        for td in trs[tr]:
            ui.append(td)
        ulist.append(ui)
    for i in range(len(ulist)):
        try:

            #名称
            mc=ulist[i][3].text
            #规格型号
            ggxh=ulist[i][5].text
            pp=""
            #单位
            dw=ulist[i][7].text
            #含税价(元)
            result = ulist[i][9].img['src']
            urllib.request.urlretrieve(result, 'D:/YZM/1.jpg')
            #历史价
            #备注
            bz=ulist[i][13].text

            print(str(categoryId),mc)
            # href = ulist[i][11].a['href']
        except Exception as e:

            # 名称
            mc = ulist[i][3].text
            # 规格型号
            ggxh = ulist[i][5].text
            # 品牌
            pp = ulist[i][7].text
            # 单位
            dw = ulist[i][9].text
            # 含税价(元)
            result = ulist[i][11].img['src']
            urllib.request.urlretrieve(result, 'D:/YZM/1.jpg')
            # 历史价
            # 备注
            bz = ulist[i][15].text
            print(str(categoryId),mc)

            # href = ulist[i][13].a['href']
        # print(str(categoryId) + "_" + href)
        db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='gcw')
        cursor = db.cursor()
        insert_color = ("INSERT INTO gcw_(time,categoryId,mc,ggxh,pp,dw,hsj,bz)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        data_color = ('201702', str(categoryId),mc,ggxh,pp,dw,python_baidu(),bz)
        cursor.execute(insert_color, data_color)
        db.commit()


        # w_url(href,driver,categoryId)
    # driver.quit()


if __name__ == '__main__':

    city=[
        40,#石家庄市
        65,#唐山市
        81,#秦皇岛市
        90,#邯郸市
        111,#邢台市
        132,#保定市
        159,#张家口市
        178,#承德市
        191,#沧州市
        209,#廊坊市
        221 #衡水市
    ]

    categoryId=[
        # #土建材料
        # 190098,#钢材
        # 190099,#钢构件制作
        # 190101,#水泥
        # 190102,#商品混凝土砂浆
        # 190103,#地材
        # 190104,#防水
        # 190105,#保温
        # 190106,#墙体材料
        #建安材料
        196215,#
        196216,#
        196217,#
        196218,#
        196219,#
        196220,#
        196221,#
        196222,#
        196223,#
        #装饰材料
        196206,#
        196207,#
        196208,#
        196209,#
        196210,#
        196211,#
        196212,#
        196213,#
        196214,#
        #机械租赁
        191828,

    #     #安装材料
    #     190116,#电线电缆
    #     190117,#电缆桥架、穿线管
    #     190120,#钢塑复合管及管件
    #     190121,#聚丁稀（PB）管及管件
    #     190122,#PE-RT地板采暖管及管件
    #     190123,#PE给水管及管件
    #     190124,#PP-R冷热水管及管件
    #     190125,#PP-R塑铝稳态复合管
    #     190126,#UPVC阻燃电线管及管件
    #     190127,#UPVC排水管及管件
    #     190129,#HDPE双壁波纹管
    #     190131,#阀门
    #     190132,#卫生洁具
    #     190133,#保温管
    #     190134,#消防器材
    #     190135,#散热器
    # #     市政材料
    #     190137,
    # #   劳务价格
    #     190140,
    # #    租赁价格
    #     190141
    ]



    # categoryId = [
    #     191923,
    #     191925,
    #     191926,
    #     191927,
    #     191928,
    #     191929,
    #     191930,
    #     191931,
    #     191932,
    #     191933,
    #     191934,
    #     191935,
    #     191936,
    #     191937,
    #     191938,
    #     191939,
    #     191940,
    #     191941,
    #     191942,
    #     191943,
    #     191944,
    #     191945,
    #     191949
    # ]

    # for i_d in range(len(categoryId)):
    #     print(categoryId[i_d])
    #     if categoryId[i_d]==191923 or categoryId[i_d]==191949:
    #         categoryLevel=1
    #     else:
    #         categoryLevel=2
    #     response = requests.get(
    #         'http://info.gldjc.com/info_price/so.html?periodId=88517&level=1&p=1&categoryId=' + str(
    #             categoryId[i_d]) + '&locationId=39&categoryLevel=' + str(categoryLevel) + '&major=全部',
    #         headers=headers())
    #     if response.status_code != 200:
    #         response.encoding = 'utf-8'
    #         print(response.status_code)
    #         print('ERROR')
    #     soup = BeautifulSoup(response.text, 'lxml')
    #     # print(soup)
    #     page = math.ceil(int(soup.find(attrs={'class': 'info_price_sum'}).strong.string) / 20)
    #
    #     for i in range(1, int(page) + 1):
    #         time.sleep(7)
    #         run(i,categoryId[i_d],categoryLevel)

