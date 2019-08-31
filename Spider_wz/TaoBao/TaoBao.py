#coding=utf8
import urllib
import urllib2
import lxml.etree
import tool_headers

#1.设置请求搜索关键词
postdate="滑膜炎"
#2.设置请求链接为手机端淘宝,并且对url进行转码和关键词追加(此链接可以简写 明天再搞)
url="https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q=%E6%BB%91%E8%86%9C%E7%82%8E&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=11&wlsort=11&page=1 "


#3.设置data数据
postdatas={
    "event_submit_do_new_search_auction":1,
    "_input_charset":"utf-8",
    "topSearch":"1",
    "atype":"b",
    "searchfrom":"1",
    "action":"home:redirect_app_action",
    "from":"1",
    "q":postdate,
    "sst":"1",
    "n":"20",
    "buying":"buyitnow",
    "m":"api4h5",
    "abtest":"11",
    "wlsort":"11",
    "page":"1"
}
date = urllib.urlencode(postdatas)

#3.发送请求 获取请求数据
request = urllib2.Request(url=url,data=date,headers=tool_headers.tool_headers())
re = urllib2.urlopen(request)
html = re.read()
# print(html)
#4.获取数据
print(html)