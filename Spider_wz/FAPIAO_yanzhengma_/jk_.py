# coding=utf-8
from flask import Flask,jsonify,request
from flask_cors import CORS
import time
import mysql.connector
import tesserocr
import json
from PIL import Image
from selenium import webdriver
from openpyxl import load_workbook
import threading
#
data = {
    'main':'Hello'
        }

app = Flask(__name__,)
# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
CORS(app, resources=r'/*')
@app.route('/get_user',methods=['GET','POST'])          #指定接口访问的路径，支持什么请求方式get，post
#讲的是封装成一种静态的接口，无任何参数传入
def get_user():
    driver = webdriver.Firefox()  # 打开火狐浏览器
    # driver=webdriver.PhantomJS(executable_path="C:\Python36\Scripts\phantomjs.exe")
    driver.get('http://fpcx.hebds.gov.cn/fpxx/fpxxcx.jsp')  # 打开界面

    if request.method == "POST":
        fpdm = request.form.get('fpdm')
        fphm = request.form.get('fphm')
        dwmc = request.form.get('dwmc')

    if request.method == "GET":
        fpdm = request.args.get('fpdm')
        fphm = request.args.get('fphm')
        dwmc = request.args.get('dwmc')

    print(fpdm,fphm,dwmc)

    driver.find_element_by_id('fpdm').send_keys(fpdm)
    driver.find_element_by_id('fphm').send_keys(fphm)
    driver.find_element_by_id('dwmc').send_keys(dwmc)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[4]/table/tbody/tr/td[2]/a').click()
    time.sleep(2)
    driver.maximize_window()
    driver.save_screenshot('D:/YZM/s1.png')  # 截取当前网页，该网页有我们需要的验证码
    imgelement = driver.find_element_by_id('cfd')
    location = imgelement.location  # 获取验证码x,y轴坐标
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    print(int(location['x']), int(location['y']), int(location['x'] + size['width']),
          int(location['y'] + size['height']))
    i = Image.open('D:/YZM/s1.png')  # 打开截图
    result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    result.save('D:/YZM/1.png')

    image = Image.open('D:/YZM/1.png')
    result = tesserocr.image_to_text(image)
    print(result)
    driver.find_element_by_id('validateCode').send_keys(result)
    driver.find_element_by_id('cxButton').click()
    time.sleep(10)
    # 收款单位
    skdw = driver.find_element_by_id('dw').get_attribute('value')
    # 主管税务机关
    zgswjg = driver.find_element_by_id('swjg').get_attribute('value')
    # 发票代码
    fpdm = driver.find_element_by_id('cxfpdm').get_attribute('value')
    # 发票号码
    fphm = driver.find_element_by_id('cxfphm').get_attribute('value')
    # 购票日期
    gprq = driver.find_element_by_id('kprq').get_attribute('value')
    # 开票金额
    kpje = driver.find_element_by_id('kpje').get_attribute('value')
    # 发票状态
    fpzt = driver.find_element_by_id('fpzt').get_attribute('value')
    # 查询次数
    cxcs = driver.find_element_by_id('cxcs').get_attribute('value')
    # 付款单位名称
    fkdwmc = driver.find_element_by_id('fkdwmc').get_attribute('value')
    # 付款单位识别号
    fkdwsbh = driver.find_element_by_id('fkdwsbh').get_attribute('value')
    # 非定额发票
    fdefp = driver.find_element_by_id('me').get_attribute('value')
    #
    print(skdw, zgswjg, fpdm, fphm, gprq, kpje, fpzt, cxcs, fkdwmc, fkdwsbh, fdefp)
    driver.close()
    return  json.dumps({
        'skdw':skdw,
        'zgswjg':zgswjg,
        'fpdm':fpdm,
        'fphm':fphm,
        'gprq':gprq,
        'kpje':kpje,
        'fpzt':fpzt,
        'cxcs':cxcs,
        'fkdwmc':fkdwmc,
        'fkdwsbh':fkdwsbh,
        'fdefp':fdefp
    },ensure_ascii=False)    #把字典转成json串返回


app.run(host='192.168.1.209',port=8080,debug=True)