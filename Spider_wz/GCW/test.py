# # coding=utf-8
#
# from selenium import webdriver
# import time
# browser=webdriver.Firefox()
# browser.maximize_window() # 窗口最大化
#
# browser.get('https://www.baidu.com') # 在当前浏览器中访问百度
#
# # 新开一个窗口，通过执行js来新开一个窗口
# js='window.open("https://www.sogou.com");'
# browser.execute_script(js)
#
# print(browser.current_window_handle) # 输出当前窗口句柄（百度）
# handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
# print(handles) # 输出句柄集合
#
# for handle in handles:# 切换窗口（切换到搜狗）
#     if handle!=browser.current_window_handle:
#         print('switch to ',handle)
#         browser.switch_to_window(handle)
#         print(browser.current_window_handle) # 输出当前窗口句柄（搜狗）
#
#         break
# time.sleep(3)
# print(browser.page_source)
# browser.close() #关闭当前窗口（搜狗）
# browser.switch_to_window(handles[0]) #切换回百度窗口
# import time
# time.sleep(10)
# browser.quit()


# -*- coding: UTF-8 -*_
from PIL import Image
from PIL import ImageFilter
from pytesseract import *
import PIL.ImageOps
#
# def initTable(threshold=140):
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     return table
#
# im = Image.open('D:/YZM/1.jpg')
# #图片的处理过程
# im = im.convert('L')
# binaryImage = im.point(initTable(), '1')
# im1 = binaryImage.convert('L')
# im2 = PIL.ImageOps.invert(im1)
# im2.save('D:/YZM/test_1.png')
# im3 = im2.convert('1')
# im2.save('D:/YZM/test_2.png')
# im4 = im3.convert('L')
# im2.save('D:/YZM/test_3.png')
# print(pytesseract.image_to_string(im2))
# #将图片中字符裁剪保留
# box = (120,0,265,60)
# region = im4.crop(box)
# region.save('D:/YZM/test_4.png')
#
# fc = region.crop((0,0,48,60))
# fc.save('D:/YZM/test_fc.png')
# op = region.crop((48,0,68,60))
# op.save('D:/YZM/test_op.png')
# region.save('test_region.png')
# lc = region.crop((68,0,120,60))
# lc.save('D:/YZM/test_lc.png')
# print(pytesseract.image_to_string(fc, config='-psm 6  -c tessedit_char_whitelist="0123456789"'))
# print(pytesseract.image_to_string(op, config='-psm 7  -c tessedit_char_whitelist="+-*/%"'))
# print(pytesseract.image_to_string(lc, config='-psm 6  -c tessedit_char_whitelist="0123456789"'))
#
# invImg = PIL.ImageOps.invert(region)
# invImg.save('D:/YZM/test_5.png')
# print(pytesseract.image_to_string(invImg, config='-psm 7  -c tessedit_char_whitelist="0123456789+-*/"'))
#
# invIm2 = invImg.convert('RGB').filter(ImageFilter.SHARPEN)
# invIm2.save('D:/YZM/test_6.jpg')
# #将图片字符放大
# out = region.resize((120,38))
# out.save('D:/YZM/test_7.png')
# # out.save('test_6.png')
# asd = pytesseract.image_to_string(out)
# print(asd)

def main():
    try:
        from PIL import Image
        import pytesseract
        text = pytesseract.image_to_string(Image.open('2.png'), lang='chi_sim')
        return text
    except Exception as e:
        return 0
print(main())