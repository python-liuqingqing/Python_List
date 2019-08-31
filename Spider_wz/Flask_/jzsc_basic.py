# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

headers = {'Host': 'jzsc.mohurd.gov.cn',
           'Origin': 'http://jzsc.mohurd.gov.cn',
           'Referer': 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/list',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

url = 'http://jzsc.mohurd.gov.cn/dataservice/query/project/projectDetail/3709021806150101'

d = pq(url, headers=headers, verify=False)
    #项目编号
xmbh = d('.activeTinyTabContent>dl>dd').eq(0).text().replace('项目编号：','')
    #省级项目编号
sjxmbh = d('.activeTinyTabContent>dl>dd').eq(1).text().replace('省级项目编号：','')
    #所在区划
szqh = d('.activeTinyTabContent>dl>dd').eq(2).text().replace('所在区划：','')
    #建设单位
jsdw = d('.activeTinyTabContent>dl>dd').eq(3).text().replace('建设单位：','')
    #建设单位组织机构代码（统一社会信用代码）
shxydm = d('.activeTinyTabContent>dl>dd').eq(4).text().replace('建设单位组织机构代码（统一社会信用代码）：','')
    #项目分类
xmfl = d('.activeTinyTabContent>dl>dd').eq(5).text().replace('项目分类：','')
    #建设性质
jsxz = d('.activeTinyTabContent>dl>dd').eq(6).text().replace('建设性质：','')
    #工程用途
gcyt = d('.activeTinyTabContent>dl>dd').eq(7).text().replace('工程用途：','')
    #总投资
ztz = d('.activeTinyTabContent>dl>dd').eq(8).text().replace('总投资：','')
    #总面积
zmj = d('.activeTinyTabContent>dl>dd').eq(9).text().replace('总面积：','')
    #立项级别
lxjb = d('.activeTinyTabContent>dl>dd').eq(10).text().replace('立项级别：','')
    #立项文号
lxwh = d('.activeTinyTabContent>dl>dd').eq(11).text().replace('立项文号：','')

print(xmbh,sjxmbh,szqh,jsdw,shxydm,xmfl,jsxz,gcyt,ztz,zmj,lxjb,lxwh)

    # 招投标 tab_ztb
ztb = d('#tab_ztb>table>tbody>tr')
for l in range(ztb.length):
    # < th > 序号 < / th >
    xh = ztb.eq(l).children('td').eq(0).text().strip()
    # < th > 招标类型 < / th >
    zblx = ztb.eq(l).children('td').eq(1).text().strip()
    # < th > 招标方式 < / th >
    zbfs = ztb.eq(l).children('td').eq(2).text().strip()
    # < th > 中标单位名称 < / th >
    zbdwmc = ztb.eq(l).children('td').eq(3).text().strip()
    zbdwmc_url = ztb.eq(l).children('td').eq(3).children('a').attr('href')
    # < th > 中标日期 < / th >
    zbrq = ztb.eq(l).children('td').eq(4).text().strip()
    # < th > 中标金额（万元） < / th >
    zbje = ztb.eq(l).children('td').eq(5).text().strip()
    # < th > 中标通知书编号 < / th >
    zbtzsbh = ztb.eq(l).children('td').eq(6).text().strip()
    # < th > 省级中标通知书编号 < / th >
    sjzbtzsbh = ztb.eq(l).children('td').eq(7).text().strip()
    # < th > < nobr > 查看 < / nobr > < / th >
    ck = ztb.eq(l).children('td').eq(8).children('a').attr('data-url')
    print("招投标")
    print(xh,zblx,zbfs,zbdwmc,zbdwmc_url,zbrq,zbje,zbtzsbh,sjzbtzsbh,ck)

    # 施工图审查 tab_sgtsc
sgtsc = d('#tab_sgtsc>table>tbody>tr')
for l in range(sgtsc.length):
    # 序号
    xh = sgtsc.eq(l).children('td').eq(0).text().strip()
    # 施工图审查合格书编号
    sgtschgsbh = sgtsc.eq(l).children('td').eq(1).text().strip()
    #省级施工图审查合格书编号
    sjsgtschgsbh = sgtsc.eq(l).children('td').eq(2).text().strip()
    #勘察单位名称
    kcdwmc = sgtsc.eq(l).children('td').eq(3).text().strip()
    kcdwmc_url = sgtsc.eq(l).children('td').eq(3).children('a').attr('href')
    #设计单位名称
    sjdwmc  = sgtsc.eq(l).children('td').eq(4).text().strip()
    sjdw_url = sgtsc.eq(l).children('td').eq(4).children('a').attr('href')
    #施工图审查机构名称
    sgtscjgmc = sgtsc.eq(l).children('td').eq(5).text().strip()
    #审查完成日期
    scwcrq = sgtsc.eq(l).children('td').eq(6).text().strip()
    #url
    jg_url = sgtsc.eq(l).children('td').eq(7).children('a').attr('data-url')
    print("施工图审查")
    print(xh,sgtschgsbh,sjsgtschgsbh,kcdwmc,kcdwmc_url,sjdwmc,sjdw_url,sgtscjgmc,scwcrq,jg_url)

    # 合同备案 tab_htba
htba = d('#tab_htba>table>tbody>tr')
for l in range(htba.length):
    #序号
    xh = htba.eq(l).children('td').eq(0).text()
    # 合同类别
    htlb = htba.eq(l).children('td').eq(1).text()
    # 合同备案编号
    htbabh = htba.eq(l).children('td').eq(2).text()
    # 省级合同备案编号
    sjhtbabh = htba.eq(l).children('td').eq(3).text()
    # 合同金额（万元）
    htje = htba.eq(l).children('td').eq(4).text()
    # 合同签订日期
    htqdrq = htba.eq(l).children('td').eq(5).text()
    # 查看
    ck_url =htba.eq(l).children('td').eq(6).children('a').attr('data-url')
    print('合同备案')
    print(xh,htlb,htbabh,sjhtbabh,htje,htqdrq,ck_url)

    # 施工许可 tab_sgxk
sgxk = d('#tab_sgxk>table>tbody>tr')
for l in range(sgxk.length):
    # 序号
    xh = sgxk.eq(l).children('td').eq(0).text()
    # 施工许可证编号
    sgxkzbh = sgxk.eq(l).children('td').eq(1).text()
    # 省级施工许可证编号
    sjsgxkzbh = sgxk.eq(l).children('td').eq(2).text()
    # 合同金额（万元）
    htje =  sgxk.eq(l).children('td').eq(3).text()
    # 面积（平方米）
    mj =  sgxk.eq(l).children('td').eq(4).text()
    # 发证日期
    fzrq =  sgxk.eq(l).children('td').eq(5).text()
    # 查看
    ck =  sgxk.eq(l).children('td').eq(6).children('a').attr('data-url')
    print("施工许可")
    print(xh,sgxkzbh,sjsgxkzbh,htje,mj,fzrq,ck)

    # 竣工验收备案 tab_jgysba
jgysba = d('#tab_jgysba>table>tbody>tr')
for l in range(jgysba.length):
    # 序号
    xh = jgysba.eq(l).children('td').eq(0).text()
    # 竣工备案编号
    jgbabh = jgysba.eq(l).children('td').eq(1).text()
    # 省级竣工备案编号
    sjjgbabh = jgysba.eq(l).children('td').eq(2).text()
    # 实际造价（万元）
    sjzj = jgysba.eq(l).children('td').eq(3).text()
    # 实际面积（平方米）
    sjmj = jgysba.eq(l).children('td').eq(4).text()
    # 实际开工日期
    sjkgrq = jgysba.eq(l).children('td').eq(5).text()
    # 实际竣工验收日期
    sjjgrq = jgysba.eq(l).children('td').eq(6).text()
    # 查看
    ck_url = jgysba.eq(l).children('td').eq(7).children('a').attr('data-url')
    print('竣工验收备案')
    print(xh,jgbabh,sjjgbabh,sjzj,sjmj,sjkgrq,sjjgrq,ck_url)