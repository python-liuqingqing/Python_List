"""
2019-09-01文书网更新:
    加密比之前的简单了许多，可能还没更新完或有没踩到的坑。
    目前发现涉及到的主要加解密算法是DES3(DESede)。
    列表页、详情页目前只发现ciphertext参数是必传的，其他好像可有可无。
    暂时全写在一个py文件里了，模块划分后面再整理更新了(java分支也是，后面再更新)～
"""
import base64
import json
import math
import random
from datetime import datetime
from pprint import pprint

# 第三方依赖: pip install requests pycryptodomex
import requests
from Cryptodome.Cipher import DES3

from Cryptodome.Util.Padding import unpad, pad


class PageID(str):
    def __new__(cls, *args, **kwargs):
        """
        function(){
            var guid = "";
            for (var i = 1; i <= 32; i++) {
                var n = Math.floor(Math.random() * 16.0).toString(16);
                guid += n;
                // if ((i == 8) || (i == 12) || (i == 16) || (i == 20)) guid +=
                // "-";
            }
            return guid;
        }
        """
        return "".join(hex(math.floor(random.random() * 16))[2:] for _ in range(32))


class RequestVerificationToken(str):
    def __new__(cls, size: int, *args, **kwargs):
        """
        function(size) {
            var str = ""
              , arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
            for (var i = 0; i < size; i++) {
                str += arr[Math.round(Math.random() * (arr.length - 1))];
            }
            return str;
        }
        """
        arr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join(arr[round(random.random() * (len(arr) - 1))] for _ in range(size))


class CipherText(str):
    def __new__(cls, *args, **kwargs):
        return cls.cipher()

    @classmethod
    def cipher(cls) -> str:
        """
        function() {
            var date = new Date();
            var timestamp = date.getTime().toString();
            var salt = $.WebSite.random(24);
            var year = date.getFullYear().toString();
            var month = (date.getMonth()+1<10 ? "0"+(date.getMonth()+1) : date.getMonth()).toString();
            var day = (date.getDate()<10 ? "0"+date.getDate() : date.getDate()).toString();
            var iv = year+month+day;
            var enc = DES3.encrypt(timestamp,salt,iv).toString();
            var str = salt+iv+enc;
            var ciphertext = strTobinary(str);
            return ciphertext;
        }
        """
        date = datetime.now()
        timestamp = str(int(date.timestamp() * 1000))
        salt = RequestVerificationToken(24)
        iv = date.strftime("%Y%m%d")
        enc = des3encrypt(plain_text=timestamp, key=salt, iv=iv)
        string = salt + iv + enc
        cipher_text = cls.str2binary(string)
        return cipher_text

    @staticmethod
    def str2binary(string: str) -> str:
        """
        function(str) {
            var result = [];
            var list = str.split("");
            for(var i = 0; i < list.length; i++) {
                if(i != 0){
                    result.push(" ");
                }
                var item = list[i];
                var binaryStr = item.charCodeAt().toString(2);
                result.push(binaryStr);
            };
            return result.join("");
        }
        """
        return " ".join(bin(ord(item))[2:] for item in string)


def des3encrypt(plain_text: str, key: str, iv: str) -> str:
    des3 = DES3.new(key=key.encode(), mode=DES3.MODE_CBC, iv=iv.encode())
    encrypted_data = des3.encrypt(pad(plain_text.encode(), DES3.block_size))
    cipher_text = base64.b64encode(encrypted_data).decode()
    return cipher_text


def des3decrypt(cipher_text: str, key: str, iv: str) -> str:
    des3 = DES3.new(key=key.encode(), mode=DES3.MODE_CBC, iv=iv.encode())
    decrypted_data = des3.decrypt(base64.b64decode(cipher_text))
    plain_text = unpad(decrypted_data, DES3.block_size).decode()
    return plain_text


class Demo:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        })

    def list_page(self):
        """文书列表页"""
        url = "http://wenshu.court.gov.cn/website/parse/rest.q4w"
        data = {
            "pageId": PageID(),
            "sortFields": "s50:desc",
            "ciphertext": CipherText.cipher(),
            "pageNum": 50,
            "pageSize": 20,
            "queryCondition": json.dumps([{"key":"s21","value":"安徽"},{"key":"cprq","value":"2013-09-02 TO 2019-09-02"}], ensure_ascii=False),  # 查询条件: s8=案件类型, 03=民事案件
            "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc",
            "__RequestVerificationToken": RequestVerificationToken(24),
        }

        response = self.session.post(url, data=data)
        json_data = response.json()
        str_data = des3decrypt(json_data["result"], json_data["secretKey"], datetime.now().strftime("%Y%m%d"))
        print(str_data)
        json_data_list = json.loads(str_data)['queryResult']['resultList']
        for item in json_data_list:
            # 裁判要旨段原文
            try:
                cpyzdyw = item["26"]
            except:
                cpyzdyw = ""

            # 文书ID
            cipher_text = item["rowkey"]
            # 案件类型
            ajlx = item["43"]
            # 裁判日期
            cprq = item["31"]
            # 案件名称
            ajmc = item["1"]
            # 案号
            ah = item["7"]
            # 法院名称
            fymc = item["2"]


            try:
                aw = item['10']
            except:
                aw = ""

            try:
                bw = item['44']
            except:
                bw = ""
            try:
                cw = item['9']
            except:
                cw = ""

            xq = ""
            mydict = {
                "cpyzdyw": cpyzdyw,
                "ajlx": ajlx,
                "cprq": cprq,
                "ajmc": ajmc,
                "ah": ah,
                "fymc": fymc,
                "wsid": cipher_text,
                "xq": "",
                "a":aw,
                "b":bw,
                "c":cw
            }

            print(mydict)


    def detail_page(self):
        """文书详情页"""
        url = "http://wenshu.court.gov.cn/website/parse/rest.q4w"
        data = {
            "docId": "1dcc417fd5d34a1f987caab100c0c8ef",
            "ciphertext": CipherText.cipher(),
            "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch",
            "__RequestVerificationToken": RequestVerificationToken(24),
        }

        response = self.session.post(url, data=data)
        json_data = response.json()
        str_data = des3decrypt(json_data["result"], json_data["secretKey"], datetime.now().strftime("%Y%m%d"))
        pprint(json.loads(str_data))


if __name__ == '__main__':
    # n = ["袭警"]
    # for s in n:
    # request_list("0")

    # start = '2018-01-06'
    # end = '2018-12-31'
    # begin_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    # end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    # while begin_date <= end_date:
    #     date_str = begin_date.strftime("%Y-%m-%d")
    #     date_list.append(date_str)
    #     begin_date += datetime.timedelta(days=1)
    # # # print(date_list[0])
    # # # # print(request_list())
    # #
    # for l in range(len(date_list)):
    #     # print(date_list[l])
    # #     # 进行数据目录的数据获取
    #     if(request_list(date_list[l])==200):
    #         continue

    demo = Demo()
    demo.list_page()
    # demo.detail_page()