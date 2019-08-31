# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import json
import time
import requests
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery as pq

app = Flask(__name__)
app.debug = True

# 搜狐房产网
@app.route('/select/lp/', methods=['post'])
def add_stu():
    if not request.data:  # 检测是否有数据
        return ('fail')
    data_ = request.data.decode('raw_unicode_escape')
    print(data_)
    data_s = json.loads(data_)
    qy = data_s['qy']
    xm_name = data_s['xm_name']
    url = 'https://'+qy+'.focus.cn/loupan/?q='+xm_name
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'gr_user_id=42c79ca6-f453-42b9-8082-eaadf245cc42; 87a4bcbf0b1ea517_gr_session_id=1a011159-1792-464e-a96b-b3fb7b3e8acf; grwng_uid=c835e43e-5924-43bf-abd3-5c9e358b536c; 87a4bcbf0b1ea517_gr_session_id_1a011159-1792-464e-a96b-b3fb7b3e8acf=true; sohu_CID=046496c6cc400f9a; IPLOC=CN3709; SUV=1905280826060KFH; focus_pc_city_p=cangzhou; focus_city_p=cangzhou; focus_city_c=130900; focus_city_s=cangzhou; pc_ad_feed=0; ad_strw=3e; focusbels=0'
    }
    res = pq(url, headers=headers, verify=False)

    xm_url = res('.s-left-menu').next('div').find('.img').children('a').attr('href')
    data_lat = res('.s-left-menu').next('div').find('.location').children('a').attr('data-lat')
    data_lon = res('.s-left-menu').next('div').find('.location').children('a').attr('data-lon')
    if(xm_url==None):
        print("抱歉，没有找到相关楼盘。")
        return json.dumps("抱歉，没有找到相关楼盘。", ensure_ascii=False)
    else:
        xq_url = xm_url.replace('.html','/xiangqing.html')
        xq_res = pq(xq_url, headers=headers, verify=False)
        jb = xq_res('#baseinfo').children('table').children('tbody').children('tr')
        # -------------------基本信息------------------
        # 楼盘名称
        lpmc = jb.eq(1).children('td').eq(1).text()
        # 建成年代
        jcnd = jb.eq(1).children('td').eq(3).text()
        # 物业类型
        wylx  = jb.eq(2).children('td').eq(1).text()
        # 项目特色
        xmts = jb.eq(2).children('td').eq(3).text()
        # 建筑类型
        jzlx = jb.eq(3).children('td').eq(1).text()
        # 装修标准
        zxbz = jb.eq(3).children('td').eq(3).text()
        # 产权年限
        cqnx = jb.eq(4).children('td').eq(1).text()
        # 专修情况
        zxqk = jb.eq(4).children('td').eq(3).text()
        # 开发商
        kfs = jb.eq(5).children('td').eq(1).text()
        # 环线位置
        hxwz = jb.eq(5).children('td').eq(3).text()
        # 投资商
        tzs = jb.eq(6).children('td').eq(1).text()
        # 品牌商
        pps = jb.eq(7).children('td').eq(1).text()
        # 楼盘地址
        lpwz = jb.eq(8).children('td').eq(1).text()

        #-----------------------销售信息-----------------------
        xs = xq_res('#saleinfo').children('table').children('tbody').children('tr')
        # 销售状态
        xszt = xs.eq(0).children('td').eq(1).text()
        # 开盘时间
        kpsj = xs.eq(1).children('td').eq(1).text()
        # 交房时间
        jfsj = xs.eq(1).children('td').eq(3).text()
        # 售楼地址
        sldz = xs.eq(2).children('td').eq(1).text()
        # 售楼电话
        sldh = xs.eq(2).children('td').eq(3).text()

        # ------------------预售许可证
        #
        xkz = xq_res('#saleinfo').find('.table-hasline').children('tbody').children('tr')
        xkz_list=[]
        xkz_list.clear()
        for l in range(xkz.length):
        #许可证号
            xkzh = xkz.eq(l).children('td').eq(0).text()
        #获取时间
            hqsj = xkz.eq(l).children('td').eq(1).text()
        #绑定楼栋
            bdld = xkz.eq(l).children('td').eq(2).text()
            xkz_list.append({
                "xkzh":xkzh,
                "hqsj":hqsj,
                "bdld":bdld
            })

        # -----------------价格信息---------------------
        jg = xq_res('#prizeinfo').find('.table-hasline').children('tbody').children('tr')
        prizeinfo=[]
        for h in range(jg.length):
        #记录时间
            jlsj = jg.eq(h).children('td').eq(0).text()
        #历史高价
            lsgj = jg.eq(h).children('td').eq(1).text()
        #均价
            jj = jg.eq(h).children('td').eq(2).text()
        #历史低价
            lsdj = jg.eq(h).children('td').eq(3).text()
        #价格描述
            jgms = jg.eq(h).children('td').eq(4).text()
            prizeinfo.append({
                "jlsj":jlsj,
                "lsgj":lsgj,
                "jj":jj,
                "lsdj":lsdj,
                "jgms":jgms
            })

        #----------------------------规划信息--------------------
        gh = xq_res('#supportinfo').children('table').children('tbody').children('tr')
        #占地面积
        zdmj = gh.eq(0).children('td').eq(1).text()
        #建筑面积
        jzmj = gh.eq(0).children('td').eq(3).text()
        #容积率
        rjl = gh.eq(1).children('td').eq(1).text()
        #绿化率
        lhl = gh.eq(1).children('td').eq(3).text()
        #停车位
        tcw = gh.eq(2).children('td').eq(1).text()
        #楼栋总数
        ldzs = gh.eq(2).children('td').eq(3).text()
        #总户数
        zhs = gh.eq(3).children('td').eq(1).text()
        #物业公司
        wygs = gh.eq(3).children('td').eq(3).text()
        #物业费
        wyf = gh.eq(4).children('td').eq(1).text()
        #物业描述
        wyms = gh.eq(5).children('td').eq(1).text()
        #周边配套
        zbpt = gh.eq(6).children('td').eq(1).text()
        #学校
        xx = gh.eq(7).children('td').eq(1).text()
        #内部配套
        nbpt = gh.eq(8).children('td').eq(1).text()
        #建材设备
        jcsb = gh.eq(9).children('td').eq(1).text()
        #供暖方式
        gnfs = gh.eq(10).children('td').eq(1).text()


        # -----------------------------楼盘简介--------------------------
        lpjj = xq_res('#lpdes').text()

        data_all = {
            "lpmc": lpmc,
            # 建成年代
            "jcnd": jcnd,
            # 物业类型
            "wylx": wylx,
            # 项目特色
            "xmts": xmts,
            # 建筑类型
            "jzlx": jzlx,
            # 装修标准
            "zxbz": zxbz,
            # 产权年限
            "cqnx": cqnx,
            # 专修情况
            "zxqk": zxqk,
            # 开发商
            "kfs": kfs,
            # 环线位置
            "hxwz": hxwz,
            # 投资商
            "tzs": tzs,
            # 品牌商
            "pps": pps,
            # 楼盘地址
            "lpwz": lpwz,
            "xszt": xszt,
            "kpsj": kpsj,
            "jfsj": jfsj,
            "sldz": sldz,
            "sldh": sldh,
            "zdmj": zdmj,
            # 建筑面积
            "jzmj": jzmj,
            # 容积率
            "rjl": rjl,
            # 绿化率
            "lhl": lhl,
            # 停车位
            "tcw": tcw,
            # 楼栋总数
            "ldzs": ldzs,
            # 总户数
            "zhs": zhs,
            # 物业公司
            "wygs": wygs,
            # 物业费
            "wyf": wyf,
            # 物业描述
            "wyms": wyms,
            # 周边配套
            "zbpt": zbpt,
            # 学校
            "xx": xx,
            # 内部配套
            "nbpt": nbpt,
            # 建材设备
            "jcsb": jcsb,
            # 供暖方式
            "gnfs": gnfs,
            # 楼盘简介
            "lpjj":lpjj,
            # 许可证
            "xkz_list":xkz_list,
            # 价格
            "prizeinfo":prizeinfo
        }

        data_lp = {
            "lpmc":lpmc,
            "url":xq_url,
            "kfs": kfs,
            "lpjj": lpjj,
            "lpwz": lpwz,
            "data_lat":data_lat,
            "data_lon":data_lon,
            "jzlx": jzlx,
            "wylx": wylx,
            "rjl": rjl,
            "lhl": lhl,
            "ldzs": ldzs,
            "zhs": zhs,
            "tcw": tcw,
            "update_time":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
            "ly":"搜狐焦点网"
        }
        return json.dumps(data_lp,ensure_ascii=False)

if __name__ == '__main__':
    # app.run(host='192.168.1.154', port=1234)
    app.run()