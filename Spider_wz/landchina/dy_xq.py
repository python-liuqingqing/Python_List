import requests
url_tid = "http://www.superfastip.com/api/ip?tid=150d1c8596f496761617ca9f8b86a6aa&type=0"
res = requests.get(url_tid)
proxy = { "http":"http://proxy.superfastip.com:7798",
        "https":"http://proxy.superfastip.com:7798"}

url = "http://www.landchina.com/default.aspx?tabid=386&comname=default&wmguid=aeb2d2f3-7519-4112-add8-7ba77dc33803&recorderguid=00001422-1281-4094-8d0d-284163c46862"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    # 'Cookie': 'ASP.NET_SessionId=oj0hdcl54wpsnm0tfpjlilhd; Hm_lvt_83853859c7247c5b03b527894622d3fa=1563089285,1563094926,1563096809,1563155919; yunsuo_session_verify=d357bd760b9a687251ad3b2d17854a22; srcurl=687474703a2f2f7777772e6c616e646368696e612e636f6d2f64656661756c742e617370783f74616269643d32363426436f6d4e616d653d64656661756c74; security_session_mid_verify=35eee97babff2056d60cc78d59578b0a; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1563156416',
    'Host': 'www.landchina.com',
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3833.0 Safari/537.36'
}
response = requests.get(url, headers=headers, proxies=proxy)
print(response.text)


#
# import requests
# import time
# url_tid = "http://www.superfastip.com/api/ip?tid=150d1c8596f496761617ca9f8b86a6aa&type=0"
# res = requests.get(url_tid)
# proxy={ "http":"http://proxy.superfastip.com:7798",
#         "https":"http://proxy.superfastip.com:7798"}
# url="http://www.httpbin.org/ip";
# # 当您的电脑第一次使用专享代理时，在30秒内可能会出现代理失败的情况，之后的访问将没有问题。
# for i in range(20):
# 	res = requests.get(url, proxies = proxy)
# 	print(res.text)
# 	time.sleep(2)