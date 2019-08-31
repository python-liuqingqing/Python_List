import requests
import re
import time
from redis import Redis
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

def push_redis_list():
    r = Redis()
    print(r.keys('*'))
    for i in range(100):
        num = 5100+i;#抓取的取件仅在5100--5200之间
        url ='http://www.meizitu.com/a/'+ str(num) +'.html'
        img_url = requests.get(url,timeout=30)
        #print img_url.text
        # #time.sleep(10)
        img_url_list = re.findall('http://pic.meizitu.com/wp-content/uploads/201.*.jpg',img_url.text)
        print(img_url_list)
        for temp_img_url in img_url_list:
            l = len(re.findall('limg',temp_img_url))
            if(l == 0):
                print("url: ",temp_img_url)
                r.lpush('meizitu',temp_img_url)
                print(r.llen('meizitu'))
        return 0
def get_big_img_url():
    r = Redis()
    print(r.keys('*'))
    while(1):
        try:
            url = r.lpop('meizitu')
            download(url)
            time.sleep(1)
            print(url)
        except:
            print("请求求发送失败重试")
            time.sleep(10)
            continue
    return 0
def download(url):
    try:
        r = requests.get(url,headers=headers,timeout = 50)
        name = int(time.time())
        f = open('./pic/'+str(name)+'.jpg','wb')
        f.write(r.content)
        f.close()
    except(Exception):
        print(Exception,":")
if __name__ == '__main__':
    url = 'http://www.meizitu.com/a/list_1_'
    print("begin")
    push_redis_list(5100)#开启则加任务队列.其中的值请限制在5400以内。不过是用于计算页码的
    #get_big_img_url()#开启则运行爬取任务