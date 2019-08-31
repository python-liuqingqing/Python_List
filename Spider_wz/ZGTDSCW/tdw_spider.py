# coding:utf-8

from lxml import etree
import requests
import time
import pymysql
import uuid
import random
import signal
import urllib
from urllib.parse import quote
import re
import ZGTDSCW.zd
import ZGTDSCW.zds
# from log import *
from collections import OrderedDict
# from fake_useragent import UserAgent

# ua=UserAgent()

proxySwitch = True
# connect = pymysql.connect(
#             host='192.168.18.213',
#             db='bobd',
#             port=3306,
#             user='root',
#             passwd='root',
#             charset='utf8',
#             use_unicode=True)
# cursor = connect.cursor()

def get_cookies(proxy):
    try:
        baseurl = 'http://www.landchina.com/default.aspx?tabid=263&ComName=defaulthttp%3a%2f%2fwww.landchina.com%2fdefault.'
        headers= {
            # 'User-Agent':ua.random,
            'Host': 'www.landchina.com'
        }
        response1 = requests.get(baseurl, headers=headers, timeout=20)
        cookies = dict(response1.cookies)
        print(cookies)
        return cookies
    except:
        print('获取cookie出错')
        return get_cookies(proxy)

def parse_list():

    headers = {
        # 'User-Agent': ua.random,
        'Host': 'www.landchina.com'
    }
    zdb=ZGTDSCW.zd.zd
    zdsf=ZGTDSCW.zds.zds
    for keys in zdsf:
        pass
    for key in zdb:
        zd1 = zdb[key].encode("unicode_escape")
        dq=quote(zd1).replace('5C', '')

        url = 'http://www.landchina.com/default.aspx?tabid=263&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&p=9f2c3acd-0256-4da2-a659-6949c4671a2a%3A2018-2-1%7E2018-3-31%7C42ad98ae-c46a-40aa-aacc-c0884036eeaf%3a'+str(key)+'%u2593~'+str(dq)
        print(url)
        # proxy = {'http': 'http://H9K26R70BM421W2D:2548D6AA73D229E3@http-dyn.abuyun.com:9020'}
        # print(proxy)
        # cookies = get_cookies(proxy)

        data = {
        '__VIEWSTATE': '/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFqAFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHRodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vZGVmYXVsdC4vVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBacBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0aHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL2RlZmF1bHQuL1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2pnZ2dfMDEuZ2lmKTsfAwUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwF + gY8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8 + PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE4IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI + DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn + WcsOW4guWcuue9kSZuYnNwOyZuYnNwO + aKgOacr + aUr + aMgTrmtZnmsZ / oh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDs8YnIgLz4NCuWkh + ahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8 + DQo8L3NwYW4 + Jm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8 + DQombmJzcDs8L3NwYW4 + PC9wPh8BBYUBQkFDS0dST1VORC1JTUFHRTp1cmwoaHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL1VzZXIvZGVmYXVsdGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9kZWZhdWx0Li9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjdzIwMTNfeXdfMS5qcGcpO2RkxaHVvbPGaFJBtezBDwhj0Bl2sysYSpQFdWFPO8G2 + js =',
        '__EVENTVALIDATION': '/wEWAgLw+ceWCQLN3cj/BCqsKpGl3TGIWs3C2IkrkdVc9VUIU9SS7i2R9raDGeAR',
        'hidComName': 'defaulthttp://www.landchina.com/default.',
        'TAB_QuerySubmitConditionData':'',
        'TAB_QuerySubmitOrderData':'',
        'TAB_RowButtonActionControl':'',
        'TAB_QuerySubmitPagerData': 1,
        'TAB_QuerySubmitSortData':'',
        }
        try:
            response = requests.get(url, headers=headers,data=data)
        except:
            pass
        # print(response.text.encode())
        lxml_response1 = etree.HTML(response.text)

        try:
            link_name=lxml_response1.xpath('//*[@id="mainModuleContainer_485_1113_1539_tdExtendProContainer"]//tr[2]/td/div//tr/td[1]/text()')[0]
            totalCount = re.findall(u"^共(\d+)页.*?", link_name)
            lent=totalCount[0]
        except:
            lent=1
        for i in range(1,int(lent)+1):
            data2 = {
                '__VIEWSTATE': '/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFqAFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHRodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vZGVmYXVsdC4vVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBacBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0aHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL2RlZmF1bHQuL1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2pnZ2dfMDEuZ2lmKTsfAwUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwF + gY8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8 + PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE4IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI + DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn + WcsOW4guWcuue9kSZuYnNwOyZuYnNwO + aKgOacr + aUr + aMgTrmtZnmsZ / oh7vlloTnp5HmioDogqHku73mnInpmZDlhazlj7gmbmJzcDs8YnIgLz4NCuWkh + ahiOWPtzog5LqsSUNQ5aSHMDkwNzQ5OTLlj7cg5Lqs5YWs572R5a6J5aSHMTEwMTAyMDAwNjY2KDIpJm5ic3A7PGJyIC8 + DQo8L3NwYW4 + Jm5ic3A7Jm5ic3A7Jm5ic3A7PGJyIC8 + DQombmJzcDs8L3NwYW4 + PC9wPh8BBYUBQkFDS0dST1VORC1JTUFHRTp1cmwoaHR0cDovL3d3dy5sYW5kY2hpbmEuY29tL1VzZXIvZGVmYXVsdGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9kZWZhdWx0Li9VcGxvYWQvc3lzRnJhbWVJbWcveF90ZHNjdzIwMTNfeXdfMS5qcGcpO2RkxaHVvbPGaFJBtezBDwhj0Bl2sysYSpQFdWFPO8G2 + js =',
                '__EVENTVALIDATION': '/wEWAgLw+ceWCQLN3cj/BCqsKpGl3TGIWs3C2IkrkdVc9VUIU9SS7i2R9raDGeAR',
                'hidComName': 'defaulthttp://www.landchina.com/default.',
                'TAB_QuerySubmitConditionData': '',
                'TAB_QuerySubmitOrderData': '',
                'TAB_RowButtonActionControl': '',
                'TAB_QuerySubmitPagerData': i,
                'TAB_QuerySubmitSortData': '',
            }
            # proxy1 = {'http': 'http://H9K26R70BM421W2D:2548D6AA73D229E3@http-dyn.abuyun.com:9020'}
            # cookies1 = get_cookies(proxy1)
            # print(proxy1)

            try:
                response2 = requests.get(url, headers=headers, data=data2, timeout = 100)
            except:
                pass
            lxml_response = etree.HTML(response2.text)
            link_list = lxml_response.xpath('//table[@id="TAB_contentTable"]/tbody//td/a/@href')

            for link in link_list:
                # time.sleep(random.randint(3, 10))
                link = 'http://www.landchina.com/'+link
                item = {}

                try:
                    response = requests.get(link, headers=headers, allow_redirects=False,timeout = 100)
                    print(response.status_code)
                    lxml_response = etree.HTML(response.content)
                    item['city']=zdb[key]
                    item['province']=zdsf[zdb[key]]
                    try:
                        district = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl"]//text()')[0]
                        item['district'] = district  # 行政区
                    except:
                        item['district']=''
                    try:
                        superviseId = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c4_ctrl"]//text()')[0]
                        item['superviseId']=superviseId  # 电子监管号
                    except:
                        item['superviseId'] = ''
                    try:
                        proName = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r17_c2_ctrl"]/text()')[0]
                        item['proName'] = proName  # 项目名称
                    except:
                        item['proName'] = ''
                    try:
                        proSite = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r16_c2_ctrl"]/text()')[0]
                        item['proSite'] = proSite  # 项目位置
                    except:
                        item['proSite'] = ''
                    try:
                        landArea = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl"]/text()')[0]
                        item['landArea'] = landArea  #  土地面积(公顷)
                    except:
                        item['landArea'] = ''
                    try:
                        landSource =re.findall('.*?areaS2.innerHTML="(.*?)";.*?',response.text)[0]
                        item['landSource'] = landSource  # 土地来源
                    except:
                        item['landSource'] = ''
                    try:
                        landPurpose = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c2_ctrl"]/text()')[0]
                        item['landPurpose'] = landPurpose  # 土地用途
                    except:
                        item['landPurpose'] = ''
                    try:
                        supplyWay = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctrl"]/text()')[0]
                        item['supplyWay'] = supplyWay  # 供地方式
                    except:
                        item['supplyWay'] = ''
                    try:
                        landLimit = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctrl"]/text()')[0]
                        item['landLimit'] = landLimit  # 土地使用年限
                    except:
                        item['landLimit'] = ''
                    try:
                        industry = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c4_ctrl"]/text()')[0]
                        item['industry'] = industry  # 行业分类
                    except:
                        item['industry'] = ''
                    try:
                        landGrade = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c2_ctrl"]/text()')[0]
                        item['landGrade'] = landGrade  # 土地级别
                    except:
                        item['landGrade'] = ''
                    try:
                        tstPrice = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c4_ctrl"]/text()')[0]
                        item['tstPrice'] = tstPrice  # 成交价格(万元)
                    except:
                        item['tstPrice'] = ''
                    try:
                        landPolur = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r9_c2_ctrl"]/text()')[0]
                        item['landPolur'] = landPolur  # 土地使用权人
                    except:
                        item['landPolur'] = ''
                    try:
                        avrLower = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c2_ctrl"]/text()')[0]
                        item['avrLower'] = avrLower  # 约定容积率-下限
                    except:
                        item['avrLower'] = ''
                    try:
                        avrUpper = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f2_r1_c4_ctrl"]/text()')[0]
                        item['avrUpper'] = avrUpper  # 约定容积率-上限
                    except:
                        item['avrUpper'] = ''
                    try:
                        aLandDate = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r21_c4_ctrl"]/text()')[0]
                        item['aLandDate'] = aLandDate  # 约定交地时间
                    except:
                        item['aLandDate'] = ''
                    try:
                        aStartDate = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c2_ctrl"]/text()')[0]
                        item['aStartDate'] = aStartDate  # 约定开工时间
                    except:
                        item['aStartDate'] = ''
                    try:
                        aCompletionDate = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c4_ctrl"]/text()')[0]
                        item['aCompletionDate'] =  aCompletionDate  # 约定竣工时间
                    except:
                        item['aCompletionDate'] = ''
                    try:
                        atStartDate = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c2_ctrl"]/text()')[0]
                        item['atStartDate'] =  atStartDate  # 实际开工时间
                    except:
                        item['atStartDate'] = ''
                    try:
                        atCompletionDate = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r10_c4_ctrl"]/text()')[0].replace("&nbsp;", "").replace("\xa0", "")
                        item['atCompletionDate'] = atCompletionDate  # 实际竣工时间
                    except:
                        item['atCompletionDate'] = ''
                    try:
                        approvedUnit = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c2_ctrl"]/text()')[0]
                        item['approvedUnit'] = approvedUnit  # 批准单位
                    except:
                        item['approvedUnit'] = ''
                    try:
                        contractDate = lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c4_ctrl"]/text()')[0]
                        item['contractDate'] = contractDate  # 合同签订日期
                    except:
                        item['contractDate'] = ''

                    item['insertDate'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 入库时间
                    item['updateDate'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 更新时间
                    item['source'] = '中国土地市场网'
                    uid = str(uuid.uuid1( ))
                    item['uid']= ''.join(uid.split('-'))
                    item['url'] = link
                    page = re.findall('<span id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_c1_\d_ctrl">(\d+)</span>', response.text)
                    print(len(page))

                    log_content_dict = OrderedDict()
                    event_name = 'zgtdw'
                    # current_id = superviseId
                    log_content_dict['url'] = link
                    log_content_dict['superviseId'] = superviseId
                    log_content_dict['status_code'] = response.status_code
                    log_content_dict['city'] = zdb[key]
                    # logging(event_name, log_content_dict)

                    for x in range(0, (len(page))):
                        try:
                            paymentIssue=lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_{}"]/td[1]//text()'.format(x))[0]
                            item['paymentIssue']=paymentIssue
                        except:
                            item['paymentIssue'] = ''
                        try:
                            aPaymentDate = lxml_response.xpath(
                                '//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_{}"]/td[2]//text()'.format(x))[0]
                            item['aPaymentDate']=aPaymentDate
                        except:
                            item['aPaymentDate']=''
                        try:
                            aPaymentAmount=lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_{}"]/td[3]//text()'.format(x))[0]
                            item['aPaymentAmount']=aPaymentAmount
                        except:
                            item['aPaymentAmount']=''
                        try:
                            remarks=lxml_response.xpath('//*[@id="mainModuleContainer_1855_1856_ctl00_ctl00_p1_f3_r2_{}"]/td[4]//text()'.format(x))[0]
                            item['remarks']=remarks
                        except:
                            item['remarks']=''

                        if item['aPaymentDate'] != '':
                            print('')
                                # cursor.execute("""select * from tdscw_paymentagreement where superviseId = %s AND aPaymentAmount=%s AND paymentIssue=%s""",
                                #                (item["superviseId"] ,item['aPaymentAmount'],item['paymentIssue']))
                                # rst = cursor.fetchone( )
                                # if rst:
                                #     cursor.execute(
                                #         """update tdscw_paymentagreement set paymentIssue = %s, aPaymentDate = %s, superviseId = %s,
                                #             aPaymentAmount = %s, remarks = %s ,uid=%s,insertDate=%s where superviseId = %s AND aPaymentAmount=%s AND paymentIssue=%s""",
                                #         (
                                #             item['paymentIssue'],
                                #             item['aPaymentDate'],
                                #             item['superviseId'],
                                #             item['aPaymentAmount'],
                                #             item['remarks'],
                                #             item['uid'],
                                #             item['insertDate'],
                                #             item['superviseId'],
                                #             item['aPaymentAmount'],
                                #             item['paymentIssue'],
                                #         )
                                #     )
                                # else:
                                #     cursor.execute("""insert into tdscw_paymentagreement(paymentIssue,aPaymentDate,aPaymentAmount,remarks,superviseId,uid,insertDate)
                                #                             values (%s,%s,%s,%s,%s,%s,%s)""",
                                #                     (
                                #                         item['paymentIssue'],
                                #                         item['aPaymentDate'],
                                #                         item['aPaymentAmount'],
                                #                         item['remarks'],
                                #                         item['superviseId'],
                                #                         item['uid'],
                                #                         item['insertDate'],
                                #
                                #                     ))
                                # connect.commit( )
                except:
                    print('{0}失败'.format(url))
                print(item)
            # except:
            #     pass

                try:
                    print('')
                    # cursor.execute("""select * from tdscw_landgrant where superviseId = %s""", item["superviseId"])
                    # ret = cursor.fetchone( )
                    # # print(ret)
                    # if ret:
                    #     cursor.execute(
                    #         """update tdscw_landgrant set uid = %s,superviseId = %s, district = %s,
                    #                                         proName = %s, proSite = %s,landArea = %s, landSource = %s, landPurpose = %s,
                    #                                          supplyWay = %s, landLimit = %s, industry = %s, landGrade = %s,tstPrice=%s, landPolur = %s, avrLower = %s, avrUpper = %s, aLandDate = %s,
                    #                                          aStartDate = %s, aCompletionDate = %s, atStartDate = %s, atCompletionDate = %s, approvedUnit = %s, contractDate = %s, insertDate = %s,
                    #                                          updateDate = %s, source = %s, url = %s,province=%s,city=%s where superviseId = %s""",
                    #         (item['uid'],
                    #          item['superviseId'],
                    #          item['district'],
                    #          item['proName'],
                    #          item['proSite'],
                    #          item['landArea'],
                    #          item['landSource'],
                    #          item['landPurpose'],
                    #          item['supplyWay'],
                    #          item['landLimit'],
                    #          item['industry'],
                    #          item['landGrade'],
                    #          item['tstPrice'],
                    #          item['landPolur'],
                    #          item['avrLower'],
                    #          item['avrUpper'],
                    #          item['aLandDate'],
                    #          item['aStartDate'],
                    #          item['aCompletionDate'],
                    #          item['atStartDate'],
                    #          item['atCompletionDate'],
                    #          item['approvedUnit'],
                    #          item['contractDate'],
                    #          item['insertDate'],
                    #          item['updateDate'],
                    #          item['source'],
                    #          item['url'],
                    #          item['province'],
                    #          item['city'],
                    #          (item['superviseId'])
                    #          ))
                    # else:
                    #     cursor.execute(
                    #         """insert into tdscw_landgrant(uid,superviseId,district,proName,proSite,landArea,
                    #                 landSource,landPurpose,supplyWay,landLimit,industry,landGrade,tstPrice,landPolur,
                    #                 avrLower,avrUpper,aLandDate,aStartDate,aCompletionDate,atStartDate,atCompletionDate,
                    #                 approvedUnit,contractDate,insertDate,updateDate,source,url,province,city) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    #         (item['uid'],
                    #          item['superviseId'],
                    #          item['district'],
                    #          item['proName'],
                    #          item['proSite'],
                    #          item['landArea'],
                    #          item['landSource'],
                    #          item['landPurpose'],
                    #          item['supplyWay'],
                    #          item['landLimit'],
                    #          item['industry'],
                    #          item['landGrade'],
                    #          item['tstPrice'],
                    #          item['landPolur'],
                    #          item['avrLower'],
                    #          item['avrUpper'],
                    #          item['aLandDate'],
                    #          item['aStartDate'],
                    #          item['aCompletionDate'],
                    #          item['atStartDate'],
                    #          item['atCompletionDate'],
                    #          item['approvedUnit'],
                    #          item['contractDate'],
                    #          item['insertDate'],
                    #          item['updateDate'],
                    #          item['source'],
                    #          item['url'],
                    #          item['province'],
                    #          item['city']
                    #          )
                    #     )
                    # connect.commit()
                except:
                    pass

if __name__ == "__main__":
    parse_list()





