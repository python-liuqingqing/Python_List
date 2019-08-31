# coding=utf-8
import urllib2
import re
import time
import redis

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36'}
job_redis = redis.Redis(host='127.0.0.1') # host为主机的IP，port和db为默认值


class Clawer(object):

    identity = 'master'  # 或slaver

    def __init__(self):
        if self.identity == 'master':
            for i in range(20):  # 将需爬取的糗事百科前20页的url并存入urls集合
                url = 'http://www.qiushibaike.com/hot/page/%d/' % (i + 1)
                job_redis.sadd('urls', url)
        self.main()

    def get_content(self):
        """
        从糗事百科中获取故事
        :return: 故事列表
        """
        stories = []
        content_pattern = re.compile('<div class="content">([\w\W]*?)</div>([\w\W]*?)class="stats"') # 匹配故事内容（第一空）和是否含有图片（第二空）的模板
        pattern = re.compile('<.*?>') # 匹配包括括号及括号内无关内容的模板
        url = job_redis.spop('urls')
        while url: # 当数据库还存在网页url，取出一个并爬取
            try:
                request = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(request)
                text = response.read()
            except urllib2.URLError, e: # 若出现网页读取错误捕获并输出
                if hasattr(e, "reason"):
                    print e.reason
            content = re.findall(content_pattern, text) # 获取含模板内容的列表
            for x in content:
                if "img" not in x[1]: # 过滤含图片的故事
                    x = re.sub(pattern, '', x[0])
                    x = re.sub('\n', '', x)
                    stories.append(x)
            url = job_redis.spop('urls')
            time.sleep(3)

        return stories

    def main(self):
        self.get_content()

if __name__ == '__main__':
    Clawer()