import requests
import re
import json
import csv
import time
def get_table(page):
    params={
        'type': 'CWBB_LRB20',
        'token': '70f12f2f4f091e459a279469fe49eca5',
        'st': 'noticedate',
        'sr': -1,
        'p': page,
        'ps': 50,
        'js': 'var lgOOHuun={pages:(tp),data: (x),font:(font)}',
        'filter': '(reportdate=^2018-09-30^)',
        'rt': 51627772
    }
    url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?'
    response = requests.get(url, params=params).text
    pat = re.compile('var.*?{pages:(\d+),data:.*?')
    page_all = re.search(pat, response)

    pattern = re.compile('var.*?data:(.*),font:(.*)}', re.S)
    items = re.search(pattern, response)
    data = items.group(1)
    code = items.group(2)
    code = json.loads(code)

    # 抓取数据时，发现数字文本都用字体文件代替，只能抓到对应的数字编码，然后需要作转换
    new_code = {}
    if code['FontMapping']:
        code = json.loads(code)
        code = code['FontMapping']
        for c in code:
            new_code[c['code']] = str(c['value'])
        for c in new_code:
            data = data.replace(c, new_code[c])
            print(data)
    data = json.loads(data)
    return page_all, data, page

def write_header(data):
    with open('A.csv', 'a', encoding='utf_8_sig', newline='') as f:
        headers = list(data[0].keys())
        writer = csv.writer(f)
        writer.writerow(headers)
def write_table(data):
    for d in data:
        with open('A.csv', 'a', encoding='utf_8_sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(d.values())

def main(page):
    data = get_table(page)

if __name__ == '__main__':
    start_time = time.time()  # 下载开始时间
    # 写入表头
    write_header(get_table(1))
    page_all = get_table(1)[0]
    page_all = int(page_all.group(1))
    for page in range(1, page_all):
        main(page)
    end_time = time.time() - start_time  # 结束时间
    print('下载用时: {:.1f} s' .format(end_time))