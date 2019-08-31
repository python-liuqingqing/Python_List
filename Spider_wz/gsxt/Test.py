# -*- coding: utf-8 -*-
import requests
import json

if __name__ == '__main__':
    url = 'https://app.gsxt.gov.cn/gsxt/cn/gov/saic/web/controller/PrimaryInfoIndexAppController/search?page=1'
    body = json.loads(
        '{"searchword":"泰安协同软件","conditions":{"excep_tab":"0","ill_tab":"0","area":"0","cStatus":"0","xzxk":"0","xzcf":"0","dydj":"0"},"sourceType":"I"}')
    data_ = json.dumps(body, ensure_ascii=False)  # 控制转json后的乱码
    headers = {
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

    response = requests.post(url, data=data_.encode('utf-8'), headers=headers, verify=False)
    # 返回信息
    versionInfo = response.text
    versionInfoPython = json.loads(versionInfo)
    dataList = versionInfoPython['data']['result']
    print(dataList['data'][0])