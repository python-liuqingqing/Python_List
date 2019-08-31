# import requests
# import time
# url_tid = "http://www.superfastip.com/api/ip?tid=5315bc263fec21aa9e1b76f8c5083896&type=1"
# res = requests.get(url_tid)
# proxy = {"http":"http://proxy.superfastip.com:7798",
#         "https":"http://proxy.superfastip.com:7798"}
# print(proxy)
# url="http://www.landchina.com/default.aspx?tabid=386&comname=default&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=2a67d1be-0dc6-4961-a51f-91cc099ecb42";
# # 当您的电脑第一次使用专享代理时，在30秒内可能会出现代理失败的情况，之后的访问将没有问题。
# for i in range(20):
# 	header = {
#
# 	}
# 	res = requests.get(url,headers=header, proxies = proxy)
# 	print(res.text)
# 	time.sleep(2)
for i in range(0,45):
	print(i)