import pymysql

conn=pymysql.connect(host='222.223.238.158', port=3306, user='cygp4_test',
        password='GF6aBm8FbN7Xf4Ff',
        db='cygp4_test',
        charset='utf8')

cursor=conn.cursor()
cursor.execute('SELECT COUNT(*) FROM niel_tmp')
# cursor.execute('SELECT * FROM niel_tmp ORDER BY id')
c1=cursor.fetchone()
cursor.execute('SELECT COUNT(*) FROM ydhxg_tesezhibiao_debug')
c2=cursor.fetchone()
print("人数 {}，人次 {}".format(c1[0],c2[0]))

from datetime import date, timedelta # 从包导入类
# import datetime         # 导入包
import time

today=date.today().timetuple()
today=time.mktime(today)
today=int(today)
tomorrow=today+24*60*60
print(tomorrow)