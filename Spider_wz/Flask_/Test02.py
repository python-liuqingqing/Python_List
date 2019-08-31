# -*- coding: utf-8 -*-
import requests, json

data = {
    # 'qy': 'hn',
    # 'xm_name': '千江悦'
    'name':'潍坊万鼎置业有限公司',
    # 'bs':2,
    # 'xmmc':'天悦府 福园',
    # 'page':0
}
url = 'http://127.0.0.1:5000/bgjl_api/'
# url = 'http://192.168.1.125:8090/ftx_api/'
r = requests.post(url, data=json.dumps(data))
versionInfoPython = json.loads(r.text)
print(versionInfoPython)
# dataList = versionInfoPython['data']['result']
# pripid = dataList['data'][0]['pripid']

# 企业基础信息
# url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-  -entbaseInfo-'+pripid+'.html?nodeNum=370000&entType=1130&sourceType=W'
# 股东信息
# url = "https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-shareholder-"+pripid+".html?nodeNum=370000&entType=1&sourceType=W"
# print(url)