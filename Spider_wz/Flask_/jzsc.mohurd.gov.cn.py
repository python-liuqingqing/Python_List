# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree
# 项目目录信息获取;
headers = {'Host': 'jzsc.mohurd.gov.cn',
           'Origin': 'http://jzsc.mohurd.gov.cn',
           'Referer': 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/list',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

data = {
    'jsxm_region_id': '',
    '$total': '',
    '$reload': 0,
    'jsxm_region': '',
    'jsxm_name': '创业家园',
    'cons_name': '',
    '$pg': 1,
    '$pgsz': 50
}

url = 'http://jzsc.mohurd.gov.cn/dataservice/query/project/list'
response = requests.post(url, data=data, headers=headers, verify=False)
if response.status_code == 200:
    response.encoding = 'utf-8'
    page = response.text
    html = etree.HTML(response.content.decode('utf-8'))
    #  数据解析
    table = html.xpath("//table/tbody/tr")  # XPath定位到表格，因为页面只有一个表格，所以直接//table，
    # 如果有多个表格，如取第二个表格，则写为//table[1] 偏移量为1 。我们不取表头信息，所以从tr[3]开始取，返回一个列表
    for i in table:  # 遍历tr列表
        #序号
        xh = ''.join(i.xpath(".//td[1]//text()")).strip()
        #项目编码
        xmbm = ''.join(i.xpath(".//td[2]//text()")).strip()
        #项目名称
        xmmc = ''.join(i.xpath(".//td[3]//text()")).strip()
        # 项目网址
        url ='http://jzsc.mohurd.gov.cn'+ ''.join(i.xpath(".//td[3]/a/@href")).strip()
        # 地址
        dz = ''.join(i.xpath(".//td[3]/span/text()")).strip()
        #项目类别
        xmlb = ''.join(i.xpath(".//td[4]//text()")).strip()
        #建设单位
        jsdw = ''.join(i.xpath(".//td[5]//text()")).strip()
        print(xh,xmbm,xmmc,url,dz,xmlb,jsdw)

    try:
        pc = re.findall('<div class="clearfix">.*?pc:(\d+).*?</a>', page)  # 页数
        tt = re.findall('<div class="clearfix">.*?tt:(\d+).*?</a>', page)  # 条数
        print(pc[0],tt[0])
    except Exception as error:
        print("报错")



# 项目基础信息

