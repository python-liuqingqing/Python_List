from selenium import webdriver
import time

driver = webdriver.Firefox()  # 打开火狐浏览器
# driver=webdriver.PhantomJS(executable_path="C:\Python36\Scripts\phantomjs.exe")
# driver.get('http://info.gldjc.com/history_price/index.html?id=5680638&locationId=39')  # 打开界面
driver.get('http://www.gldjc.com/login?hostUrl=http%3A%2F%2Fwww.gldjc.com%2F')
driver.find_element_by_id('userName').send_keys('vip1712210204')
driver.find_element_by_id('password').send_keys('xtrj9900')
driver.find_element_by_id('loginBtn').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/a[2]').click()
time.sleep(3)
# # 获取cookie信息
# driver.add_cookie({'name': 'gldjc_sessionid', 'value': '76ac6b19-c163-4bdd-91c5-5c3263823bdb', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': True})
# driver.add_cookie({'name': 'location_name', 'value': '%25E5%25B1%25B1%25E4%25B8%259C', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1535526815, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'location_code', 'value': '370000', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1535526815, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': '_gat_gtag_UA_110560299_1', 'value': '1', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1532935416, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'loginUuid', 'value': '76ac6b19-c163-4bdd-91c5-5c3263823bdb', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6', 'value': '1532934815', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1564470821, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6', 'value': '1532934821', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'Hm_lvt_727d5904b141f326c9cb1ede703d1162', 'value': '1532934815', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1564470821, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'Hm_lpvt_727d5904b141f326c9cb1ede703d1162', 'value': '1532934822', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'nTalk_CACHE_DATA', 'value': '{uid:kf_9318_ISME9754_6349427345656906564,tid:1532934815210575}', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': 'NTKF_T2D_CLIENTID', 'value': 'guest8E07549D-AB8C-2FD4-7DAA-EA08FDEBEEAB', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1596006822, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1924718030.1532934816', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1596006822, 'secure': False, 'httpOnly': False})
# driver.add_cookie({'name': '_gid', 'value': 'GA1.2.1604537509.1532934822', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1533021222, 'secure': False, 'httpOnly': False})
# time.sleep(3)
#
# # 打印获取的cookies信息
# driver.refresh()
cookies=driver.get_cookies()
print(cookies)
#
# import tesserocr
# from PIL import Image
# image = Image.open('D:/YZM/1.png')
# result = tesserocr.image_to_text(image)
# print(result)