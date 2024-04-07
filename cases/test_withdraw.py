import unittest
from common import readexcel
from library.ddt import ddt,data
import os
from common.handlepath import DATADIR
from common.handlelog import log
from common.handleconfig import conf
from common.handlerequests import handlerequests
import jsonpath
from common.connectdb import DB
from decimal import Decimal
import random
import logging

@ddt
class withdrawTest(unittest.TestCase):

        excel = readexcel.Readexcel(os.path.join(DATADIR,"cases.xlsx"), "withdraw")
        case_datas = excel.read_data()
        requests = handlerequests()
        db = DB()

        @data(*case_datas)
        def test_recharge(self,case_data):

            url = conf.get("env", "url") + case_data["url"]
            method = case_data["method"]
            headers = eval(conf.get("env", "headers"))
            expected = eval(case_data["expected"])



            if case_data["interface"] == "login":
                data = {"mobile_phone": conf.get("test_data", "phone"), "pwd": conf.get("test_data", "pwd")}
                response = self.requests.send(url=url, headers=headers, method=method, json=data)
                res = response.json()
                withdrawTest.member_id = jsonpath.jsonpath(res, "$..id")[0]
                token = jsonpath.jsonpath(res, "$..token")[0]
                token_type = jsonpath.jsonpath(res, "$..token_type")[0]
                withdrawTest.Authorization = token_type + " " + token



            if case_data["check_sql"]:
                sql = case_data["check_sql"].format(conf.get("test_data", "phone"))
                start_amount = self.db.find__one(sql)["leave_amount"]
                print(start_amount)

            if case_data["interface"] == "withdraw":
                headers["Authorization"] = withdrawTest.Authorization
                case_data["data"] = case_data["data"].replace("#member_id#", str(withdrawTest.member_id))
                data = eval(case_data["data"])
                response = self.requests.send(url=url, method=method, json=data, headers=headers)
                res = response.json()

            row = case_data["case_id"] + 1


            try:
                self.assertEqual(expected["code"],res["code"])
                self.assertEqual(expected["msg"], res["msg"])
                if case_data["check_sql"]:
                    sql = case_data["check_sql"].format(conf.get("test_data","phone"))
                    end_amount = self.db.find__one(sql)["leave_amount"]
                    # print(end_amount)
                    # print(end_amount - start_amount)
                    # print(Decimal(str(data["amount"])))
                    self.assertEqual( Decimal(str(data["amount"])),start_amount  - end_amount)

            except Exception as e:
                self.excel.write_data(row=row,column=8,value="未通过")
                log.error("（{}）,该用例没有通过".format(case_data["title"]))
                log.exception(e)
                raise e

            else:
                self.excel.write_data(row=row,column=8,value="通过")
                log.info("{},该用例已通过".format(case_data["title"]))


        def setUp(self):
            print("每条用例执行前都会执行一次:")

        def tearDown(self):
            print("每条用例执行后都会执行一次")

        @classmethod
        def setUpClass(cls):
            print("开始测试")

        @classmethod
        def tearDownClass(cls):
            print("结束测试:")











