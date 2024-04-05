

import pymysql
#
from common.handlerequests import handlerequests
import time
# from decimal import Decimal
#
#
conn = pymysql.connect(host="api.lemonban.com",
                       port=3306,
                       user="future",
                       password="123456",
                       charset="utf8")


cur = conn.cursor()
#
#
sql1 = "SELECT leave_amount FROM future.member WHERE mobile_phone = '13650607999'"
sql2 = "SELECT leave_amount FROM future.member WHERE mobile_phone = '13266510127'"

# sql = "SELECT id FROM future.member WHERE mobile_phone=13266510127"

# sql2 = "SELECT * FROM future.member LIMIT 100"

# sql2 = "SELECT * FROM  future.member LIMIT 10"
requests = handlerequests()
response = requests.send(url="http://api.lemonban.com/futureloan/member/recharge",method="post",json={"member_id": 183973,"amount":600},headers={"X-Lemonban-Media-Type":"lemonban.v1"})

res = cur.execute(sql1)
print(cur.fetchone())
# conn.commit()
requests = handlerequests()
response = requests.send(url="http://api.lemonban.com/futureloan/member/recharge",method="post",json={"member_id": 183973,"amount":600},headers={"X-Lemonban-Media-Type":"lemonban.v1"})
# print(res)
# time.sleep(3)
# conn.commit()
res = cur.execute(sql1)
print(cur.fetchone())
response = requests.send(url="http://api.lemonban.com/futureloan/member/recharge",method="post",json={"member_id": 183973,"amount":600},headers={"X-Lemonban-Media-Type":"lemonban.v1"})
response = requests.send(url="http://api.lemonban.com/futureloan/member/recharge",method="post",json={"member_id": 173073,"amount":600},headers={"X-Lemonban-Media-Type":"lemonban.v1"})
res = cur.execute(sql2)
print(cur.fetchone())
res = cur.execute(sql1)
print(cur.fetchone())

conn.commit()

print("最新的数据")
res = cur.execute(sql2)
print(cur.fetchone())
res = cur.execute(sql1)
print(cur.fetchone())


# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())

# print(cur.fetchall())

# f1 = 1.1
# f2 = 9.8
#
# print(f2-f1)

# D1 = Decimal(1.1)
# D2 = Decimal(9.8)
#
# print(D2)
# print(D1)
#
# print(D2-D1)
#



