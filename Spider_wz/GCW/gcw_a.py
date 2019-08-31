import requests
import urllib
from bs4 import BeautifulSoup
import re
import tesserocr
from PIL import Image
import random
import time
import math
from openpyxl import workbook  # 写入Excel表所用
from selenium import webdriver

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
        'Cookie': '_ga=GA1.2.1941771097.1532672669; NTKF_T2D_CLIENTID=guest362BED4E-82AC-A075-FCA4-DA68F5B6DCBB; location_code=130000; location_name=%E6%B2%B3%E5%8C%97%E7%9C%81; INFO_PRICE_LOCATION=39_1; bjd_zhiyin_day=2018728; bjd_zhiyin=1; isTax=0; keyword_history=%25E7%2583%25AD%25E8%25BD%25A7%25E9%2592%25A2%2C%25E4%25B8%258D%25E9%2594%2588%25E9%2592%25A2; UM_distinctid=164de8cac855fd-0457043043facd-5e442e19-1fa400-164de8cac877f; gldjc_sessionid=c57d9f20-d7aa-4190-9be1-c012e3d9ef08; Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6=1532672669,1532910467; Hm_lvt_727d5904b141f326c9cb1ede703d1162=1532672669,1532910467; _gid=GA1.2.662157881.1532910467; loginUuid=c57d9f20-d7aa-4190-9be1-c012e3d9ef08; access_token=af1808f5-1c6c-4663-a107-b57d5ca4ef6d; nTalk_CACHE_DATA={uid:kf_9318_ISME9754_6349427345656906564,tid:1532910467547369}; Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6=1532931648; Hm_lpvt_727d5904b141f326c9cb1ede703d1162=1532931648; _gat_gtag_UA_110560299_1=1'}
    return headers

def w_url(href):
    driver = webdriver.Firefox()  # 打开火狐浏览器
    driver.set_page_load_timeout(30)
    driver.get(href)  # 打开界面

    time.sleep(3)
    driver.add_cookie({'name': 'gldjc_sessionid', 'value': '39e0c310-83f6-4fd4-a10e-983392b87cc6', 'path': '/',
                       'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': True})
    driver.add_cookie(
        {'name': 'location_name', 'value': '%25E5%25B1%25B1%25E4%25B8%259C', 'path': '/', 'domain': '.gldjc.com',
         'expiry': 1535531192, 'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'location_code', 'value': '370000', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1535531192,
         'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': '_gat_gtag_UA_110560299_1', 'value': '1', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1532939793,
         'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'loginUuid', 'value': '39e0c310-83f6-4fd4-a10e-983392b87cc6', 'path': '/', 'domain': '.gldjc.com',
         'expiry': None, 'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'nTalk_CACHE_DATA', 'value': '{uid:kf_9318_ISME9754_6349427345656906564,tid:1532939192431315}',
         'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
    driver.add_cookie({'name': 'NTKF_T2D_CLIENTID', 'value': 'guest6DE8EBA3-F3AF-F1D9-ECD9-EA4BC870E82E', 'path': '/',
                       'domain': '.gldjc.com', 'expiry': 1596011199, 'secure': False, 'httpOnly': False})
    driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1004482802.1532939194', 'path': '/', 'domain': '.gldjc.com',
                       'expiry': 1596011199, 'secure': False, 'httpOnly': False})
    driver.add_cookie({'name': '_gid', 'value': 'GA1.2.1482668967.1532939200', 'path': '/', 'domain': '.gldjc.com',
                       'expiry': 1533025599, 'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'INFO_PRICE_LOCATION', 'value': '1_1', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1540715203,
         'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'Hm_lvt_727d5904b141f326c9cb1ede703d1162', 'value': '1532939192', 'path': '/', 'domain': '.gldjc.com',
         'expiry': 1564475203, 'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'Hm_lpvt_727d5904b141f326c9cb1ede703d1162', 'value': '1532939203', 'path': '/', 'domain': '.gldjc.com',
         'expiry': None, 'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6', 'value': '1532939192', 'path': '/', 'domain': '.gldjc.com',
         'expiry': 1564475203, 'secure': False, 'httpOnly': False})
    driver.add_cookie(
        {'name': 'Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6', 'value': '1532939203', 'path': '/', 'domain': '.gldjc.com',
         'expiry': None, 'secure': False, 'httpOnly': False})

    time.sleep(3)
    driver.refresh()
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
    print(title)
    # com_names = soup.find_all(class_='data_table')

    wb = workbook.Workbook()  # 创建Excel对象
    ws = wb.active  # 获取当前正在操作的表对象
    # 往表中写入标题行,以列表形式写入！
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
        urllib.request.urlretrieve(result, 'D:/YZM/1.png')
        image = Image.open('D:/YZM/1.png')
        hsj = tesserocr.image_to_text(image)
        print(hsj)
        rq= ulist[i][7].text
        bz= ulist[i][8].text
        ws.append(
            [xh,mc,ggxh,dw,sl,csj,hsj,rq,bz])
        print(title)
        wb.save('1.xlsx')

    driver.close()

def run(i,categoryId):
    print('------------------第'+str(i)+"页")
    response = requests.get('http://info.gldjc.com/info_price/so.html?periodId=103185&level=1&p='+str(i)+'&categoryId='+str(categoryId)+'&locationId=39&categoryLevel=1&major=全部', headers=headers())
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
        href = ulist[i][11].a['href']
        print(href)
        w_url(href)


if __name__ == '__main__':

    categoryId = [
        191923,
        191925,
        191926,
        191927,
        191928,
        191929,
        191930,
        191931,
        191932,
        191933,
        191934,
        191935,
        191936,
        191937,
        191938,
        191939,
        191940,
        191941,
        191942,
        191943,
        191944,
        191945,
        191949
    ]
    for i_d in range(len(categoryId)):
        print(categoryId[i_d])
        if categoryId[i_d]==191923 or categoryId[i_d]==191949:
            categoryLevel=1
        else:
            categoryLevel=2
        response = requests.get(
            'http://info.gldjc.com/info_price/so.html?periodId=55573&level=1&p=1&categoryId=' + str(
                categoryId[i_d]) + '&locationId=39&categoryLevel=' + str(categoryLevel) + '&major=全部',
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
            # time.sleep(5)
            run(i, categoryId[i_d])

