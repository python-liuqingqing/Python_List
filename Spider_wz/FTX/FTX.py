# coding:utf-8
import mysql.connector
import time
from bs4 import BeautifulSoup
from selenium import webdriver

l=84  #50  61  100  101  112  113  114 116   145 147  149
jsonData=[]
json_city=[]

driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com')
def main(jsonData, l):
    print(jsonData[l].decode(),str(l))
    # 新开一个窗口，通过执行js来新开一个窗口
    print(jsonData[l].decode())
    js = 'window.open("'+jsonData[l].decode()+'");'
    driver.execute_script(js)
    handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="xfptxq_B03_08"]').click()
    except:
        driver.find_element_by_xpath('//*[@id="orginalNaviBox"]/a[2]').click()
    time.sleep(3)
    try:
        try:
            address = driver.find_element_by_xpath('//*[@id="xfzxxq_B01_03"]/p/a[3]').text
            name = driver.find_element_by_xpath('//*[@id="daohang"]/div/div/dl/dd/div[1]/h1/a').text
            # 价格
            jg = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div/div[1]/em').text
            # 物业类型
            wylx = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[1]/div[2]').text
            # 项目特色
            xmts = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[2]/div[2]').text
            # 建筑类别
            jzlb = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[3]/div[2]/span').text
            # 装修状态
            zxzt = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[4]/div[2]').text
            # 产权年限
            cqnx = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[5]/div[2]').text
            # 环线位置
            hxwz = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[6]/div[2]').text
            # 开发 商
            kfs = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[7]/div[2]').text
            # 楼盘地址
            lpdz = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/ul/li[8]/div[2]').text


            # 销售状态
            xszt = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[1]/div[2]').text
            # 楼盘优惠
            lpyh = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[2]/div[2]').text
            # 开盘时间
            kpsj = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[3]/div[2]').text
            # 交房时间
            jfsj = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[4]/div[2]').text
            # 售楼地址
            sldz = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[5]/div[2]').text
            # 咨询电话
            zxdh = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[6]/div[2]').text
            # 主力户型
            zlhx = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/ul/li[7]/div[2]').text
            try:
                try:
                    ysxkz = driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div[1]/div[2]/div/div[2]').get_attribute(
                        'innerHTML')
                except:
                    # 预售许可证
                    ysxkz = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[2]/div/div').get_attribute(
                        'innerHTML')

                soup = BeautifulSoup(ysxkz, 'lxml')
                trs = soup.select("table tbody tr")
                ysxk = []
                ulist = []
                for tr in range(len(trs)):
                    ui = []
                    for td in trs[tr]:
                        ui.append(td)
                    ulist.append(ui)
                for i in range(1, len(ulist)):
                    ysxkz_ = ulist[i][1].text
                    fzsj_ = ulist[i][3].text
                    bdld_ = ulist[i][5].text
                    ysxk.append({"ysxkz_": ysxkz_,
                                 "fzsj_": fzsj_,
                                 "bdld_": bdld_
                                 })
            except:
                ysxk = []
            print(ysxk)
            # 周边设施
            zbss = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[3]').text
            # 占地面积
            zdmj = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[1]/div[2]').text
            # 建筑面积
            jzmj = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[2]/div[2]').text
            # 容积率
            rjl = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[3]/div[2]').text
            # 绿化率
            lhl = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[4]/div[2]').text
            # 停车位
            tcw = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[5]/div[2]').text
            # 楼栋总数
            ldzs = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[6]/div[2]').text
            # 总户数
            zhs = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[7]/div[2]').text
            # 物业公司
            wygs = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[8]/div[2]').text
            # 物业费
            wyf = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[9]/div[2]').text
            # 物业费描述
            wyfms = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[10]/div[2]').text
            # 楼层状况
            lczk = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[4]/ul/li[11]/div[2]').text
            # 价格信息
            # jgxx=driver.find_element_by_xpath('').text
            # 项目简介/html/body/div[6]/div/div[1]/div[5]/p
            xmjj = driver.find_element_by_class_name('intro').text

        except:
            # 价格/html/body/div[5]/div/div[1]/div[1]/div/div/em
            address = driver.find_element_by_id('xfzxxq_B01_03').text
            name = driver.find_element_by_xpath('//*[@id="daohang"]/div/div/dl/dd/div[1]/h1/a').text

            jg = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[1]/em').text
            # 物业类型
            wylx = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[1]/div[2]').text
            # 项目特色
            xmts = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[2]/div[2]').text
            # 建筑类别
            jzlb = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[3]/div[2]/span').text
            # 装修状态
            zxzt = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[4]/div[2]').text
            # 产权年限
            cqnx = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[5]/div[2]').text
            # 环线位置
            hxwz = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[6]/div[2]').text
            # 开发 商
            kfs = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[7]/div[2]/a').text
            # 楼盘地址
            lpdz = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/ul/li[8]/div[2]').text
            # 销售状态
            xszt = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[1]/div[2]').text
            # 楼盘优惠
            lpyh = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[2]/div[2]').text
            # 开盘时间
            kpsj = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[3]/div[2]').text
            # 交房时间
            jfsj = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[4]/div[2]').text
            # 售楼地址
            sldz = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[5]/div[2]').text
            # 咨询电话
            zxdh = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[6]/div[2]').text
            # 主力户型
            zlhx = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/ul/li[7]/div[2]').text

            try:
                try:
                    ysxkz = driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div[1]/div[2]/div/div[2]').get_attribute(
                        'innerHTML')
                except:
                    # 预售许可证
                    ysxkz = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[2]/div/div').get_attribute(
                        'innerHTML')

                soup = BeautifulSoup(ysxkz, 'lxml')
                trs = soup.select("table tbody tr")
                ysxk = []
                ulist = []
                for tr in range(len(trs)):
                    ui = []
                    for td in trs[tr]:
                        ui.append(td)
                    ulist.append(ui)
                for i in range(1, len(ulist)):
                    ysxkz_ = ulist[i][1].text
                    fzsj_ = ulist[i][3].text
                    bdld_ = ulist[i][5].text
                    ysxk.append({"ysxkz_": ysxkz_,
                                 "fzsj_": fzsj_,
                                 "bdld_": bdld_
                                 })
            except:
                ysxk = []
            print(ysxk)
            # 周边设施
            zbss = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[3]').text
            # 占地面积
            zdmj = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[1]/div[2]').text
            # 建筑面积
            jzmj = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[2]/div[2]').text
            # 容积率
            rjl = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[3]/div[2]').text
            # 绿化率
            lhl = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[4]/div[2]').text
            # 停车位
            tcw = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[5]/div[2]').text
            # 楼栋总数
            ldzs = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[6]/div[2]').text
            # 总户数
            zhs = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[7]/div[2]').text
            # 物业公司
            wygs = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[8]/div[2]').text
            # 物业费
            wyf = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[9]/div[2]').text
            # 物业费描述
            wyfms = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[10]/div[2]').text
            # 楼层状况
            lczk = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[4]/ul/li[11]/div[2]').text
            # 价格信息
            # jgxx=driver.find_element_by_xpath('').text
            # 项目简介
            xmjj = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[6]').text

        z = {
            "url": jsonData[l].decode(),
            "address": address,
            "name": name,
            "jg": jg,
            # 物业类型
            "wylx": wylx,
            # 项目特色
            "xmts": xmts,
            # 建筑类别
            "jzlb": jzlb,
            # 装修状态
            "zxzt": zxzt,
            # 产权年限
            "cqnx": cqnx,
            # 环线位置
            "hxwz": hxwz,
            # 开发 商
            "kfs": kfs,
            # 楼盘地址
            "lpdz": lpdz,
            # 销售状态
            "xszt": xszt,
            # 楼盘优惠
            "lpyh": lpyh,
            # 开盘时间
            "kpsj": kpsj,
            # 交房时间
            "jfsj": jfsj,
            # 售楼地址
            "sldz": sldz,
            # 咨询电话
            "zxdh": zxdh,
            # 主力户型
            "zlhx": zlhx,
            "ysxk": ysxk,

            # 周边设施
            "zbss": zbss,
            # 占地面积
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
            # 物业费描述
            "wyfms": wyfms,
            # 楼层状况
            "lczk": lczk,
            # 项目简介
            "xmjj": xmjj

        }
        print(z)

        import pymongo

        myclient = pymongo.MongoClient("mongodb://192.168.1.19:27017/")
        mydb = myclient["ftx"]
        mycol = mydb["ftx_dz"]
        mydict = z
        x = mycol.insert_one(mydict)

        driver.close()
        driver.switch_to_window(handles[0])
        l += 1
        time.sleep(2)
        main(jsonData, l)
    except:
        driver.close()
        driver.switch_to_window(handles[0])
        with open("err.txt", "a") as f:
            f.writelines(str(l)+",")
        l += 1
        time.sleep(2)
        main(jsonData, l)
        print("报错！！！")



if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='master')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT href,city FROM ftx_href_dz"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果
    for row in results:
        result = {}
        city_list = {}
        result = row[0]
        city_list = row[1]
        jsonData.append(result)
        # json_city.append(city_list)
    main(jsonData, l)
    print(len(results))
    # try:

    # except:
    #     print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()