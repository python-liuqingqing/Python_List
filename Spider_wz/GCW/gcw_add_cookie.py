from selenium import webdriver
import time

driver = webdriver.Firefox()  # 打开火狐浏览器
driver.get('http://info.gldjc.com/history_price/index.html?id=5680638&locationId=39')  # 打开界面
time.sleep(3)
driver.add_cookie({'name': 'gldjc_sessionid', 'value': '39e0c310-83f6-4fd4-a10e-983392b87cc6', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': True})
driver.add_cookie({'name': 'location_name', 'value': '%25E5%25B1%25B1%25E4%25B8%259C', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1535531192, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'location_code', 'value': '370000', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1535531192, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': '_gat_gtag_UA_110560299_1', 'value': '1', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1532939793, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'loginUuid', 'value': '39e0c310-83f6-4fd4-a10e-983392b87cc6', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'nTalk_CACHE_DATA', 'value': '{uid:kf_9318_ISME9754_6349427345656906564,tid:1532939192431315}', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'NTKF_T2D_CLIENTID', 'value': 'guest6DE8EBA3-F3AF-F1D9-ECD9-EA4BC870E82E', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1596011199, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': '_ga', 'value': 'GA1.2.1004482802.1532939194', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1596011199, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': '_gid', 'value': 'GA1.2.1482668967.1532939200', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1533025599, 'secure': False, 'httpOnly': False},)
driver.add_cookie({'name': 'INFO_PRICE_LOCATION', 'value': '1_1', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1540715203, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'Hm_lvt_727d5904b141f326c9cb1ede703d1162', 'value': '1532939192', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1564475203, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'Hm_lpvt_727d5904b141f326c9cb1ede703d1162', 'value': '1532939203', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'Hm_lvt_82698a74ed862e6a03fc9e4cbac594a6', 'value': '1532939192', 'path': '/', 'domain': '.gldjc.com', 'expiry': 1564475203, 'secure': False, 'httpOnly': False})
driver.add_cookie({'name': 'Hm_lpvt_82698a74ed862e6a03fc9e4cbac594a6', 'value': '1532939203', 'path': '/', 'domain': '.gldjc.com', 'expiry': None, 'secure': False, 'httpOnly': False})



time.sleep(3)
driver.refresh()