import random
import requests
import math
import time
import urllib
import mysql.connector
from aip import AipOcr
from os import path
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium import webdriver

def python_baidu():
    try:
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


    except Exception as e:
        print("第二个图片识别")
        picfile = 'D:/YZM/1.jpg'
        filename = path.basename(picfile)
        APP_ID = '11651945'  # 刚才获取的 ID，下同
        API_KEY = 'euBrpM5GVVHHaeOVyPWY2z9F'
        SECRECT_KEY = 'zhMOjAa58oyYAMeZGpF1qBu0CvtrSDBY'
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
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.181.1 Safari/537.1",
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
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'location_name=%25E5%25B1%25B1%25E4%25B8%259C; location_code=370000; NTKF_T2D_CLIENTID=guest25161BD1-0B4D-D104-BD8B-C635EF2F550C; _ga=GA1.2.567991635.1536628748; _gid=GA1.2.346581333.1536628748; INFO_PRICE_LOCATION=1_1; 20180912_6349427345656906564_pop=77; gldjc_sessionid=cde096c9-362f-43f5-90b1-8fe84ad22b4d; loginUuid=cde096c9-362f-43f5-90b1-8fe84ad22b4d; Hm_lvt_727d5904b141f326c9cb1ede703d1162=1536628747,1536653839,1536711974,1536798414; Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6=1536628748,1536653839,1536711974,1536798414; _gat_gtag_UA_110560299_1=1; nTalk_CACHE_DATA={uid:kf_9318_ISME9754_6349427345656906564,tid:1536797231716071}; 20180913_6349427345656906564_pop=77; Hm_lpvt_727d5904b141f326c9cb1ede703d1162=1536798426; Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6=1536798426'}
    return headers

def run(li_title_q,title,ul_li_title,i,li_data_id_q, cid, categoryLevel):
    print('------------------第' + str(i) + "页")
    from urllib.parse import quote
    import string
    url = r'http://info.gldjc.com/info_price/so.html?periodId='+str(li_data_id_q)+'&level=2&p='+str(i)+'&categoryId='+str(cid)+'&locationId=81&categoryLevel='+str(categoryLevel)+'&major=房建'
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

            # 名称
            mc = ulist[i][3].text
            # 规格型号
            ggxh = ulist[i][5].text
            pp = ""
            # 单位
            dw = ulist[i][7].text
            # 含税价(元)
            try:
                result = ulist[i][9].img['src']
                urllib.request.urlretrieve(result, 'D:/YZM/1.jpg')
            except Exception as e:
                result = ulist[i][9].img['src']
                urllib.request.urlretrieve(result, 'D:/YZM/1.jpg')

            # 历史价
            href = ulist[i][11].a['href']
            # 备注
            bz = ulist[i][13].text

            print(li_title_q,title,ul_li_title, mc, ggxh, pp, dw, python_baidu(), bz,href)
            #
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
            href = ulist[i][13].a['href']
            # 备注
            bz = ulist[i][15].text
            print(li_title_q,title,ul_li_title, mc, ggxh, pp, dw, python_baidu(), bz,href)

        db = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='gcw')
        cursor = db.cursor()

        insert_color = ("INSERT INTO gcw_(li_title_q,title,ul_li_title,mc,ggxh,pp,dw,hsj,bz,href,zy)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data_color = (li_title_q,title,ul_li_title, mc, ggxh, pp, dw, python_baidu(), bz,href,'房建')
        cursor.execute(insert_color, data_color)
        db.commit()

def fangfa_page(li_title_q,title,ul_li_title,li_data_id_q, cid, categoryLevel):
    response = requests.get('http://info.gldjc.com/info_price/so.html?periodId='+str(li_data_id_q)+'&level=2&categoryId='+str(cid)+'&locationId=81&categoryLevel='+str(categoryLevel)+'&major=房建',
            headers=headers())
    if response.status_code != 200:
        response.encoding = 'utf-8'
        print(response.status_code)
        print('ERROR')
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    page = math.ceil(int(soup.find(attrs={'class': 'info_price_sum'}).strong.string) / 20)
    print(page)

    for i in range(1, int(page) + 1):
        time.sleep(7)
        run(li_title_q,title,ul_li_title,i,li_data_id_q, cid, categoryLevel)

if __name__ == '__main__':
    driver = webdriver.Firefox()  # 打开火狐浏览器
    driver.get('http://info.gldjc.com/info_price/so.html?level=2&locationId=81&major=房建')
    time.sleep(2)
    pageSource = driver.page_source
    d = pq(pageSource)
    # 期数 年度
    qs=d('#period_area_list>li')
    for t in range(16,17):# int(qs.length)
        #年度期数
        li_title_q = qs.eq(t).children('a').attr('title')
        print(li_title_q)
        li_data_id_q = qs.eq(t).children('a').attr('data-id')
        href = 'http://info.gldjc.com/info_price/so.html?periodId='+li_data_id_q+'&level=2&locationId=81&major=房建'
        js = 'window.open("'+str(href)+'");'
        driver.execute_script(js)
        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        for handle in handles:  # 切换窗口（切换到搜狗）
            if handle != driver.current_window_handle:
                driver.switch_to_window(handle)
        time.sleep(3)
        page_ = driver.page_source
        b = pq(page_)
        # 左侧菜单信息（分类）
        li_=b('#treeTag>li')
        for i in range(2,int(b('#treeTag>li').length)+1):#int(b('#treeTag>li').length)+1
            bool_zt = b('#treeTag>li:nth-of-type(' + str(i) + ')').children('ul').has_class('level0')
            title = b('#treeTag>li:nth-of-type(' + str(i) + ')').children('a').attr('title')
            if(bool_zt):
                ul_li = b('#treeTag>li:nth-of-type(' + str(i) + ')').children('ul>li')
                for i in range(int(ul_li.length)):#
                    # print(li_title_q)
                    # print(li_data_id_q)
                    cid = ul_li.eq(i).attr('cid')
                    ul_li_title=ul_li.eq(i).children('a').attr('title')
                    print(title)
                    categoryLevel = 2
                    fangfa_page(li_title_q,title,ul_li_title,li_data_id_q,cid,categoryLevel)
            else:
                cid=b('#treeTag>li:nth-of-type(' + str(i) + ')').attr('cid')
                print(title)
                categoryLevel = 1
                try:
                    ul_li_title = ul_li.eq(i).children('a').attr('title')
                except Exception as e:
                    ul_li_title = 0

                fangfa_page(li_title_q,title,ul_li_title,li_data_id_q, cid, categoryLevel)

        driver.close()
        driver.switch_to_window(handles[0])



