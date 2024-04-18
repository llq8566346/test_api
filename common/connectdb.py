import pymysql

from common.handleconfig import conf

class DB:

    def __init__(self):

        self.conn = pymysql.connect(
                       host=conf.get("db","host"),
                       port=conf.getint("db","port"),
                       user=conf.get("db","user"),
                       password=conf.get("db","password"),
                       charset=conf.get("db","charset"),
                       cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def find__one(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        # self.conn.commit()
        return data

    def find__all(self,sql):
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def find__count(self,sql):
        self.conn.commit()
        data = self.cur.execute(sql)
        return data

    def close(self):
        self.conn.close()
        self.cur.close()



# a = DB()
#
# sql = "SELECT * FROM future.member WHERE mobile_phone=13650607999"
#
# b = a.find__count(sql)
# print(type(b))















