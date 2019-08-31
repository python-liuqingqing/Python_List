# coding=utf-8
import time
import mysql.connector
import pytesseract
from PIL import Image
from selenium import webdriver
from pyquery import PyQuery as pq
import datetime

driver = webdriver.Chrome()  # 打开火狐浏览器
# driver=webdriver.PhantomJS(executable_path="C:\Python36\Scripts\phantomjs.exe")
driver.get('http://220.171.31.186:86/search/presell.jsp')  # 打开界面
date_list = []
def ff(time_):
    try:
        js = 'window.open("http://220.171.31.186:86/search/presell.jsp");'
        driver.execute_script(js)
        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        for handle in handles:  # 切换窗口（切换到搜狗）
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
        time.sleep(3)

        driver.find_element_by_id('keys').send_keys(time_)
        s = driver.find_element_by_xpath('//*[@id="cxform"]/table/tbody/tr[2]/td[2]/select')
        s.find_element_by_xpath('//option[@value="5"]').click()
        time.sleep(2)
        driver.maximize_window()
        driver.save_screenshot('s'+str(1)+'.png')  # 截取当前网页，该网页有我们需要的验证码
        imgelement = driver.find_element_by_id('codeimg')
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        print(int(location['x']), int(location['y']), int(location['x'] + size['width']),int(location['y'] + size['height']))
        i = Image.open('s'+str(1)+'.png')  # 打开截图
        result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        result.save('1.png')
        time.sleep(5)
        image = Image.open('1.png')
        result = pytesseract.image_to_string(image)
        print(result)
        driver.find_element_by_id('checkCode').send_keys(result)
        driver.find_element_by_xpath('//*[@id="cxform"]/table/tbody/tr[4]/td/input[1]').click()
        time.sleep(3)
        text = driver.switch_to_alert().text
        if(text=='true'):
            print("正常运行！！！！")
            driver.switch_to_alert().accept() # 点击弹出里面的确定按钮
            time.sleep(3)
            html = driver.execute_script("return document.documentElement.outerHTML")
            res = pq(html)
            t_count = res('#response').children('table')
            for t in range(len(t_count)):
                print(t)
                # 项目名称
                xmmc = t_count.eq(t).children('tbody').children('tr').eq(0).children('td').eq(1).text()
                # 预售证号
                yszh = t_count.eq(t).children('tbody').children('tr').eq(0).children('td').eq(3).text()
                # 坐落位置
                zlwz = t_count.eq(t).children('tbody').children('tr').eq(1).children('td').eq(1).text()
                # 开发公司
                kfgs = t_count.eq(t).children('tbody').children('tr').eq(1).children('td').eq(3).text()
                # 用途
                yt = t_count.eq(t).children('tbody').children('tr').eq(2).children('td').eq(1).text()
                # 发证时间
                fzsj = t_count.eq(t).children('tbody').children('tr').eq(2).children('td').eq(3).text()
                print({
                    "xmmc": xmmc,
                    "yszh": yszh,
                    "zlwz": zlwz,
                    "kfgs": kfgs,
                    "yt": yt,
                    "fzsj": fzsj
                })
                driver.close()
                driver.switch_to_window(handles[0])
                return 'true'
                # driver.switch_to_alert().dismiss() # 点击弹出上面的X按钮
        elif (text == 'false'):
            print("重新运行该页面！！！")
            ff(time_)
        elif(text=='抱歉,没有找到相关的预售证信息,请核对关键字后再次尝试!'):
            print("没有数据，进行下一步操作！！！")
            return 'true'

    except Exception as e:
        driver.close()
        driver.switch_to_window(handles[0])
        ff(time_)
i=1

if __name__ == '__main__':
    start = '2018-01-28'
    end = '2018-12-31'
    begin_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    for l in range(len(date_list)):
        print(date_list[l].replace('-',''))
        if(ff(date_list[l].replace('-',''))=='true'):
            continue