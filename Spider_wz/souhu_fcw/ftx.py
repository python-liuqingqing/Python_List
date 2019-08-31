# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import json
import time
import requests
import urllib
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery as pq

app = Flask(__name__)
app.debug = True

# 房天下
@app.route('/select/lp/', methods=['post'])
def add_stu():
    if not request.data:  # 检测是否有数据
        return ('fail')
    data_ = request.data.decode('raw_unicode_escape')
    print(data_)
    data_s = json.loads(data_)
    qy = data_s['qy']
    xm_name = data_s['xm_name']
    url = 'https://'+qy+'.newhouse.fang.com/house/s/a9'+urllib.parse.quote(xm_name.encode('gb2312'))+'/?xf_source='+urllib.parse.quote(xm_name.encode('gb2312'))

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'global_cookie=trhdcj2226znypt4jzr2cziuv10jw79vo57; city=hs; new_search_uid=3c1325516e1a2b82f6d2dac3ed7bf0ad; __utma=147393320.73320776.1559022160.1559022160.1559022160.1; __utmc=147393320; __utmz=147393320.1559022160.1.1.utmcsr=hs.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; vh_newhouse=1_1559022241_3416%5B%3A%7C%40%7C%3A%5D0ae7c145bcc6463746d3c61f0bab8efa; newhouse_user_guid=42CD995B-1FE2-0108-63C1-95B2DFA2622E; newhouse_chat_guid=D82886D0-CF09-86A5-3226-51FF9CD2EC18; Captcha=7136564C30727954434C32474F57326C4C524172534579387947506A584236654F2F397043567A4D672F514A696D32326E5664706A6231546B73572F41434B695A317569327464677141673D; g_sourcepage=undefined; appLoad=1; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; unique_cookie=U_trhdcj2226znypt4jzr2cziuv10jw79vo57*11; __utmb=147393320.45.10.1559022160',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    print(url)
    res = requests.get(url, headers=headers)
    res.encoding = 'gb2312'
    tit_ = pq(res.text)
    title_url = 'https:'+tit_('#newhouse_loupai_list').children('ul').children('li').eq(0).find('.nlc_img').children('a').attr('href')
    print(title_url)
    res_ = requests.get(title_url, headers=headers)
    res_.encoding = 'gb2312'
    xq = pq(res_.text)
    xq_url = 'https:'+xq('#orginalNaviBox').children('a').eq(1).attr('href')

    res_x = requests.get(xq_url, headers=headers)
    res_x.encoding = 'gb2312'
    doc = pq(res_x.text)
    # print(doc)
    ftx_t = doc('.main-left').children('.main-item').eq(0).children('ul').children('li')
    lpbt = doc('.lpbt').children('h1').children('a').text()
    # ----------------------基本信息---------------------------
    # 物业类型
    wylx = ftx_t.eq(0).children('.list-right').text()
    # 项目特色
    xmts = ftx_t.eq(1).children('.list-right').children('span').text()
    # 建筑类别
    jzlb = ftx_t.eq(1).children('.list-right').children('li').eq(0).children('.list-right').text()
    # 装修状态
    zxzt = ftx_t.eq(1).children('.list-right').children('li').eq(1).children('.list-right').text()
    # 产权年限
    cqnx = ftx_t.eq(1).children('.list-right').children('li').eq(2).children('.list-right').text()
    # 环线位置
    hxwz = ftx_t.eq(1).children('.list-right').children('li').eq(3).children('.list-right').text()
    # 开发 商
    kfs = ftx_t.eq(1).children('.list-right').children('li').eq(4).children('.list-right-text').text()
    # 楼盘地址
    lpdz =ftx_t.eq(1).children('.list-right').children('li').eq(5).children('.list-right-text').text()

    # -------------------------小区规划----------------------------
    ftx_gh = doc('.main-left').children('.main-item').eq(0).find('.main-item').eq(2).children('ul').children('li')
    # 占地面积
    zdmj = ftx_gh.eq(0).children('.list-right').text()
    # 建筑面积
    jzmj = ftx_gh.eq(1).children('.list-right').text()
    # 容积率
    rjl = ftx_gh.eq(2).children('.list-right').text()
    # 绿化率
    lhl = ftx_gh.eq(3).children('.list-right').text()
    # 停车位
    tcw = ftx_gh.eq(4).children('.list-right').text()
    # 楼栋总数
    ldzs = ftx_gh.eq(5).children('.list-right').text()
    # 总户数
    zhs = ftx_gh.eq(6).children('.list-right').text()
    # 物业公司
    wygs = ftx_gh.eq(7).children('.list-right').text()
    # 物业费
    wyf = ftx_gh.eq(8).children('.list-right').text()
    # 物业费描述
    wyfms = ftx_gh.eq(9).children('.list-right-floor').text()
    # 楼层状况
    lczk = ftx_gh.eq(10).children('.list-right-floor').text()


    # ----------------------项目简介------------------------
    xmjj = doc('.main-left').children('.main-item').eq(0).find('.main-item').eq(4).children('.intro').text()
    # print({
    #     "lpbt":lpbt,
    #     "wylx":wylx,
    #     "xmts":xmts,
    #     "jzlb":jzlb,
    #     "zxzt":zxzt,
    #     "cqnx":cqnx,
    #     "hxwz":hxwz,
    #     "kfs":kfs,
    #     "lpdz":lpdz,
    #
    #     "zdmj":zdmj,
    #     "jzmj":jzmj,
    #     "rjl":rjl,
    #     "lhl":lhl,
    #     "tcw":tcw,
    #     "ldzs":ldzs,
    #     "zhs":zhs,
    #     "wygs":wygs,
    #     "wyf":wyf,
    #     "wyfms":wyfms,
    #     "lczk":lczk,
    #     "xmjj":xmjj
    # })


    data_lp = {
                "lpmc":lpbt,
                "url":xq_url,
                "kfs": kfs,
                "lpjj": xmjj,
                "lpwz": lpdz,
                "data_lat":'',
                "data_lon":'',
                "jzlx": jzlb,
                "wylx": wylx,
                "rjl": rjl,
                "lhl": lhl,
                "ldzs": ldzs,
                "zhs": zhs,
                "tcw": tcw,
                "update_time":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                "ly":"房天下"
            }

    return json.dumps(data_lp, ensure_ascii=False)


if __name__ == '__main__':
    # app.run(host='192.168.1.154', port=1234)
    app.run()
