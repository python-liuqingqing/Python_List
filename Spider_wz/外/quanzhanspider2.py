import requests
import re
# from lxml import etree
from time import sleep, ctime
import threading

headers = {"Mozilla/5.0": "(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"}

#进入 main方法
def get_novel_list():
    number = int(input("请输入你要爬取内容的页数："))
    for i in range(1, number + 1):
        print("-————————————————第"+str(i)+"页——————————————————")
        next_url = "https://www.qihaoqihao.com/shuku/0/weekvisit-0-%d.html" % i
        response = requests.get(next_url, headers=headers)
        response.encoding = 'gbk'
        html = response.text
        reg = r'<div class="col-md-5 col-sm-4 col-xs-9 text-overflow"><a href="(.*?)" title="(.*?)">.*?</a></div>'
        return re.findall(reg, html)
        # print(re.findall(reg,html))


def chapter_list():
    # 从在线阅读界面取出各章节地址
    response = requests.get(novel)
    response.encoding = 'utf-8'
    html = response.text
    reg = r'<dd class="col-md-3"><a href="(.*?)">(.*?)</a></dd>'
    return re.findall(reg, html)

# 详情页面获取
def get_chapter_content(chapter_url):
    print(chapter_url)

    # y=0
    # if y == 0:
    #     y=y+1
    #     response = requests.get(chapter_url)
    #     response.encoding = 'gbk'
    #     html = response.text
    #     # print(html)
    #     reg = r'<div class="panel-body" id="htmlContent">(.*?)</div>'
    #     print(re.findall(reg, html, re.S)[0])
    # else:
    #     ak = chapter_url
    #     ram = chapter_url[::-1]
    #
    #     for i in range(2, 10):
    #         a = "lmth." + str(i) + "_"
    #         rom = re.sub(r'lmth.', a, ram)
    #         chapter_url_late = rom[::-1]
    #         chapter_url = chapter_url_late
    #
    #         response = requests.get(chapter_url)
    #         response.encoding = 'gbk'
    #         html = response.text
    #         # print(html)
    #         reg = r'<div class="panel-body" id="htmlContent">(.*?)</div>'
    #         print(re.findall(reg, html, re.S)[0])

threads = []
number=[]

for novel, novel_name in get_novel_list():
    number.append(novel)
for l in range(len(number)):
    t = threading.Thread(target=get_chapter_content, args=(number[l],))
    threads.append(t)
        # chapter_content = get_chapter_content(chapter_url)
        # print(chapter_content)
    #     fn = open(novel_name + '.txt', 'a', encoding='utf-8')
    #     fn.writelines(['\n' + chapter_title + '\n', chapter_content])
    #     fn.close()
if __name__ == '__main__':
    #启动线程
    for i in range(30):
        threads[i].start()
    for i in range(30):
        threads[i].join()

    #主线程
    # print('end:%s' %ctime())

