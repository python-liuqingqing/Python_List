from aip import AipOcr
from os import path
"""利用百度api识别文本，并保存提取的文字
    picfile:    图片文件名
    outfile:    输出文件
    """
def python_baidu():
    picfile = 'D:/YZM/1.jpg'
    filename = path.basename(picfile)

    APP_ID = '10710735'  # 刚才获取的 ID，下同
    API_KEY = '42XxnGaFENV4rcWk1dFiulDZ'
    SECRECT_KEY = 'vNN9W604gIFTu4tDZ6vhxVZrzo0aPWOO'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    # message = client.basicAccurate(img)   # 通用文字高精度识别，每天 800 次免费
    for line in message["words_result"]:
        print(line["words"])
        return line["words"]
