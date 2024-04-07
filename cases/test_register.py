import unittest
# import runtest
from common import readexcel
from library.ddt import ddt,data
import os

from common.handlepath import DATADIR

from common.handlelog import log
from common.handleconfig import conf
from common.handlerequests import handlerequests
import random
import logging
@ddt
class registerTest(unittest.TestCase):

        excel = readexcel.Readexcel(os.path.join(DATADIR,"cases.xlsx"), "register")
        case_datas = excel.read_data()
        requests = handlerequests()

        @data(*case_datas)
        def test_register(self,case_data):

            phone = self.random_phone()

            case_data["data"] = case_data["data"].replace("#phone",phone)

            url = conf.get("env","url")+case_data["url"]

            method = case_data["method"]

            headers = eval(conf.get("env","headers"))

            data = eval(case_data["data"])

            expected =eval(case_data["expected"])

            response = self.requests.send(url=url,method=method,json=data,headers=headers)

            res = response.json()

            row = case_data["case_id"] + 1


            try:
                self.assertEqual(expected["code"],res["code"])
                self.assertEqual(expected["msg"], res["msg"])
            except Exception as e:
                self.excel.write_data(row=row,column=7,value="未通过")
                log.error("{},该用例没有通过".format(case_data["title"]))
                log.exception("以下是用例({})的报错信息".format(case_data["title"]))
                raise e

            else:
                self.excel.write_data(row=row,column=7,value="通过")
                log.info("{},该用例已通过".format(case_data["title"]))

        def random_phone(self):
            phone = "136"
            n = random.randint(100000000,999999999)
            phone = phone + str(n)[1:]
            return phone



        def setUp(self):
            print("每条用例执行前都会执行一次:")

        def tearDown(self):
            print("每条用例执行后都会执行一次")

        @classmethod
        def setUpClass(cls):
            print("开始测试:")

        @classmethod
        def tearDownClass(cls):
            print("结束测试:")


# excel = readexcel.Readexcel("cases.xlsx" , "register")
#
# datas = excel.read_data()
#
# print(datas)

# registerTest("test_register_pass",datas)


