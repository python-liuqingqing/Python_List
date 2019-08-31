import json
import requests
import re
from lxml import etree

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=nwa4gjphyop0eijo1vqlczkf; ASPSESSIONIDSSAQTAAS=KJIBIKFAJHGFDLLOFKBKMCMN',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
page = 4
url = 'http://www.wffdcxx.com.cn/xy/qylist.asp?page='+str(page)+'&xy_dengji='
response = requests.post(url, headers=header, verify=False)
if response.status_code == 200:
    response.encoding = 'gb2312'
    html = etree.HTML(response.text)
    #  数据解析
    table = html.xpath('/html/body/table[16]/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/text()')
    print(table)
    # for i in table:  # 遍历tr列表
    #     xh = ''.join(i.xpath(".//td[0]/b/text()")).strip()
    #     print(xh)