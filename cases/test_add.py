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
from common.handle_data import CaseData,replace_data
import random
import logging



from common.handle_sign import HandleSign




@ddt
class rechargeTest(unittest.TestCase):

        excel = readexcel.Readexcel(os.path.join(DATADIR,"cases.xlsx"), "add")
        case_datas = excel.read_data()
        requests = handlerequests()
        db = DB()

        @data(*case_datas)
        def test_recharge(self,case_data):

            url = conf.get("env","url")+case_data["url"]

            method = case_data["method"]

            headers = eval(conf.get("env","headers"))

            headers["Authorization"] = getattr(CaseData,"Authorization")

            case_data["data"] = replace_data(case_data["data"])

            data = eval(case_data["data"])

            # print(data)
            #
            # sign_info = HandleSign().generate_sign(getattr(CaseData, "token"))
            #
            # data.update(sign_info)
            #
            # print(data)

            expected =eval(case_data["expected"])

            # if case_data["check_sql"]:
            #     sql = case_data["check_sql"].format(conf.get("test_data", "mobile_phone"))
            #     start_amount = self.db.find__one(sql)["leave_amount"]
            #     print(start_amount)

            response = self.requests.send(url=url,method=method,json=data,headers=headers)

            res = response.json()

            row = case_data["case_id"] + 1

            try:
                self.assertEqual(expected["code"],res["code"])
                self.assertEqual(expected["msg"], res["msg"])
                # if case_data["check_sql"]:
                #     sql = case_data["check_sql"].format(conf.get("test_data","mobile_phone"))
                #     end_amount = self.db.find__one(sql)["leave_amount"]
                #     print(end_amount)
                    # print(end_amount - start_amount)
                    # print(Decimal(str(data["amount"])))
                    # self.assertEqual(end_amount - start_amount , Decimal(str(data["amount"])))

            except Exception as e:
                self.excel.write_data(row=row,column=8,value="未通过")
                log.error("（{}）,该用例没有通过".format(case_data["title"]))
                log.exception(e)
                log.exception(res["msg"])
                raise e

            else:
                self.excel.write_data(row=row,column=8,value="通过")
                log.info("{},该用例已通过".format(case_data["title"]))


        def setUp(self):
            pass

        def tearDown(self):
            print("每条用例执行后都会执行一次")

        @classmethod
        def setUpClass(cls):
            url =   conf.get("env","url") + "/member/login"
            headers = eval(conf.get("env","headers"))
            data = {"mobile_phone":conf.get("test_data","admin_phone"),"pwd":conf.get("test_data","admin_pwd")}
            response = cls.requests.send(url=url,headers=headers,method="post",json=data)
            res = response.json()
            member_id = jsonpath.jsonpath(res,"$..id")[0]
            token = jsonpath.jsonpath(res,"$..token")[0]
            # CaseData.token = token
            token_type = jsonpath.jsonpath(res,"$..token_type")[0]
            Authorization = token_type + " " + token
            CaseData.Authorization = Authorization
            CaseData.admin_member_id = member_id


        @classmethod
        def tearDownClass(cls):
            print("结束测试:")















