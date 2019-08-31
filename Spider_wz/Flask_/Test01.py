# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
app.debug = True


@app.route('/select/name/', methods=['post'])
def add_stu():
    if not request.data:  # 检测是否有数据
        return ('fail')
    name = request.data.decode('utf-8')
    enterprise_name = json.loads(name)
    url = 'https://app.gsxt.gov.cn/gsxt/cn/gov/saic/web/controller/PrimaryInfoIndexAppController/search?page=1'
    body = json.loads(
        '{"searchword":"'+enterprise_name["name"]+'","conditions":{"excep_tab":"0","ill_tab":"0","area":"0","cStatus":"0","xzxk":"0","xzcf":"0","dydj":"0"},"sourceType":"I"}')
    data_ = json.dumps(body, ensure_ascii=False)  # 控制转json后的乱码
    headers_a = {
        'Content-Type': 'application/raw',
        'Host': 'app.gsxt.gov.cn',
        'Cookie': 'JSESSIONID=D26788EACA25EEF8BFAA4091585D7C77; SECTOKEN=7184035096920064216; __jsluid=da5c7271631d61c4fb14a75350f62e48',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 Html5Plus/1.0',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'br, gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, data=data_.encode('utf-8'), headers=headers_a, verify=False)
    # 返回信息
    versionInfo = response.text
    versionInfoPython = json.loads(versionInfo)
    dataList = versionInfoPython['data']['result']
    # 获取所需要的唯一标示
    pripid = dataList['data'][0]['pripid']
    nodeNum = dataList['data'][0]['nodeNum']
    entType = dataList['data'][0]['entType']
    # 企业基础数据信息
    # url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-primaryinfoapp-entbaseInfo-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 股东信息
    url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-shareholder-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 年报信息
    # url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-anCheYearInfo-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 主要人员
    # url= 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-KeyPerson-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 分支机构
    # url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-branch-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 清算信息
    # url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-liquidation-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 变更信息
    # url= 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-alter-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'
    # 动产抵押登记
    # url= 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-mortreginfo-'+str(pripid)+'.html?nodeNum='+str(nodeNum)+'&entType='+str(entType)+'&start=0&sourceType=W'

    headers_b = {
        'Content-Type': 'text/html;charset=UTF-8',
        'Host': 'app.gsxt.gov.cn',
        'Cookie': 'JSESSIONID=95784B254BAFE7A9D4A55CDD013CCC7F; Path=/gsxt/; HttpOnly; SECTOKEN=7141809874888557116; Expires=Mon, 28-Apr-2087 09:49:03 GMT; Path=/;tlb_cookie=172.16.12.1078080; path=/;__jsluid=d7bb588f780a6561c0b2732501b0d28a; max-age=31536000; path=/; HttpOnly',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D39 Html5Plus/1.0',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'br, gzip, deflate',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers_b, verify=False)
    # 返回信息
    versionInfo_xq = response.text
    # print(versionInfo_xq)
    return versionInfo_xq


if __name__ == '__main__':
    # app.run(host='192.168.1.154', port=1234)
    app.run()
    # 这里指定了地址和端口号。