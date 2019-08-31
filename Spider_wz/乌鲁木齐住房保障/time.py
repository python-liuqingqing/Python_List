import datetime
date_list = []
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