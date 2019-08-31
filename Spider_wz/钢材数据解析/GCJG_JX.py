import mysql.connector
import json
import re

jsonData=[]
if __name__ == '__main__':
    # 打开数据库连接
    db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='china_gcw')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select id,title,time,list_table FROM gc_jiage"
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 打印结果
    for row in results:
        try:
            title = row[1]
            pat = re.compile("日" + '(.*?)' + "钢材", re.S)
            title = pat.findall(title)
            time = row[2]
            list_ = row[3]
            num_gc = json.loads(list_)
            for ab in range(len(num_gc)):
                #         品种
                pz = num_gc[ab]["pz"]
                #         材质
                cz = num_gc[ab]["cz"]
                #         规格
                guig = num_gc[ab]["guig"]
                #         价格
                jg = num_gc[ab]["jg"]
                #         涨跌
                zd = num_gc[ab]["zd"]
                #         钢厂、产地
                gc = num_gc[ab]["gc"]
                #         备注
                bz = num_gc[ab]["bz"]

                print({
                    "title": title[0],
                    "time": time,
                    "pz": pz,
                    "cz": cz,
                    "guig": guig,
                    "jg": jg,
                    "zd": zd,
                    "gc": gc,
                    "bz": bz
                })
                db = mysql.connector.connect(user='root', password='123456', host='192.168.1.130', database='china_gcw')
                cursor = db.cursor()
                insert_color = (
                    "INSERT INTO all_gangcai(title,time,pz,cz,guig,jg,zd,gc,bz)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                data_color = (title[0], time, pz, cz, guig, jg, zd, gc, bz)
                cursor.execute(insert_color, data_color)
                db.commit()
        except:
            continue

    print(len(results))
    db.close()