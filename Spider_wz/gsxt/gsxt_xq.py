# -*- coding: utf-8 -*-
import requests
requests.packages.urllib3.disable_warnings()

headers = {
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

pripid = "B1B49758BFA95EAA72854A845CAB78E201C7A7C7A7C724E282305030503050305C305030A0C00666D4B4D437D4B8-1554864902012"

# 基础详情信息
# url="https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-primaryinfoapp-entbaseInfo-C8CBEE27C6D627D50BFA33FB25D4019D5DCBADCBADCB0B9DFB294F254325C0A6CCA6C025A94C2ACF2ABC2AF84CDA-1554886205967.html?nodeNum=370000&entType=1130&sourceType=W"

# 股东信息
# url = "https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-shareholder-0ACB2C2704D6E5D5C9FAF1FBE7D4C39D9FCB6FCB6FCBC99D39298D25812502A60EA602256B4CE8CFE8BCE8F88EDA-1554880223571.html?nodeNum=370000&entType=1&sourceType=W"
# 年报信息
# url = "https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-anCheYearInfo-0ACB2C2704D6E5D5C9FAF1FBE7D4C39D9FCB6FCB6FCBC99D39298D25812502A60EA602256B4CE8CFE8BCE8F88EDA-1554880223571.html?nodeNum=370000&entType=1&sourceType=W"
# 主要人员
# url="https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-KeyPerson-0ACB2C2704D6E5D5C9FAF1FBE7D4C39D9FCB6FCB6FCBC99D39298D25812502A60EA602256B4CE8CFE8BCE8F88EDA-1554880223571.html?nodeNum=370000&entType=1&sourceType=W"
# 分支机构
# url = "https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-branch-0ACB2C2704D6E5D5C9FAF1FBE7D4C39D9FCB6FCB6FCBC99D39298D25812502A60EA602256B4CE8CFE8BCE8F88EDA-1554880223571.html?nodeNum=370000&entType=1&sourceType=W"
# 清算信息
# url = "https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-liquidation-9513B3FF9B0E7A0D56226E23780C5C45AACA29CA29CA2545A649AA49AA49AA4929491E49A64512FDCC2FCC2F4F5C-1554881067074.html?nodeNum=210000&entType=1&sourceType=W"
# 变更信息
# url="https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-alter-9513B3FF9B0E7A0D56226E23780C5C45AACA29CA29CA2545A649AA49AA49AA4929491E49A64512FDCC2FCC2F4F5C-1554881067074.html?nodeNum=210000&entType=1&sourceType=W"
# 动产抵押登记
#url="https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-mortreginfo-9513B3FF9B0E7A0D56226E23780C5C45AACA29CA29CA2545A649AA49AA49AA4929491E49A64512FDCC2FCC2F4F5C-1554881067074.html?nodeNum=210000&entType=1&sourceType=W"
#
# print(url)
response = requests.get('https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-shareholder-B7CB9127B9D658D574FA4CFB5AD47E9D22CBD2CBD2CB749D842930253C25BFA6B3A6BF25D64C55CF55BC55F833DA-1557295592140.html?nodeNum=370000&entType=1&sourceType=W',headers=headers,verify=False)
# 返回信息
versionInfo = response.text
print(versionInfo)


# mysql 查询连接