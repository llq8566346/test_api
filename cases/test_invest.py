

import unittest
from common.readexcel import Readexcel
from common.handlepath import DATADIR
import os
from common.connectdb import DB
from library.ddt import ddt,data
from common.handleconfig import conf
from common.handlerequests import handlerequests
from common.handle_data import CaseData,replace_data
import jsonpath
from common.handlelog import log


"""

投资接口：
1、需要有标：管理员登录，加标、审核，
2、用户登录
3、投资用例的执行

# 关于投资的sql校验语句
1、用户表、校验用户余额是否发生变化，变化金额等于所投金额（根据用户id去查member表）
SELECT * FROM future.member WHERE id={}
2、根据用户id和标id去投资表中查用户的投资记录，（invest里面查用户对应的标是否新增一条记录）
SELECT * FROM future.invest WHERE member_id={} and loan_di={}
3、根据用户id去流水标中查询流水记录（查询用户投资之后是否多了一条记录）
SELECT * FROM future.financelog WHERE pay_member_id={}
4、在刚好投满的情况下，可以根据投资记录的id，去回款计划表中查询是否，生成回款计划。
SELECT * FROM future.repayment WHERE invest_id={}

"""


@ddt
class InvestTest(unittest.TestCase):

    excel = Readexcel(os.path.join(DATADIR,"cases.xlsx"),"invest")
    case_datas = excel.read_data()
    db = DB()
    requests = handlerequests()

    @data(*case_datas)
    def test_invest(self,case_data):
        url = conf.get("env", "url") + case_data["url"]
        headers = eval(conf.get("env", "headers"))
        method = case_data["method"]
        data = eval(replace_data(case_data["data"]))
        expected = eval(case_data["expected"])
        row = case_data["case_id"] + 1

        if case_data["interface"] == "login" :
            response = self.requests.send(url=url, headers=headers, method=method, json=data)
            res = response.json()
            token = jsonpath.jsonpath(res,"$..token")[0]
            token_type = jsonpath.jsonpath(res,"$..token_type")[0]
            member_id = jsonpath.jsonpath(res,"$..id")[0]
            Authorization = token_type + " " + token
            CaseData.Authorization = Authorization
            CaseData.member_id = member_id

        if case_data["interface"] == "add" :
            headers["Authorization"] = CaseData.Authorization
            response = self.requests.send(url=url, headers=headers, method=method, json=data)
            res = response.json()
            loan_id = jsonpath.jsonpath(res,"$..id")[0]
            CaseData.loan_id = loan_id

        if case_data["interface"] == "audit" :
            headers["Authorization"] = CaseData.Authorization
            response = self.requests.send(url=url, headers=headers, method=method, json=data)
            res = response.json()

        if case_data["interface"] == "invest" :
            headers["Authorization"] = CaseData.Authorization
            if case_data["check_sql"]:
                start_invest = self.db.find__count("SELECT * FROM future.invest WHERE loan_id = {} and member_id = {}".
                                          format(CaseData.loan_id,CaseData.member_id))
                sql2 = self.db.find__one("SELECT * FROM future.member WHERE id={}".format(CaseData.member_id))
                start_log = self.db.find__count("SELECT * FROM future.financelog WHERE pay_member_id = {}".
                                                   format(CaseData.member_id))
                start_amount = sql2["leave_amount"]
            response = self.requests.send(url=url, headers=headers, method=method, json=data)
            res = response.json()

        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
            if case_data["check_sql"] :
                end_invest =  self.db.find__count("SELECT * FROM future.invest WHERE loan_id = {} and member_id = {}".
                                          format(CaseData.loan_id,CaseData.member_id))
                sql2 =  self.db.find__one("SELECT * FROM future.member WHERE id={}".format(CaseData.member_id))
                end_log = self.db.find__count("SELECT * FROM future.financelog WHERE pay_member_id = {}".
                                                format(CaseData.member_id))
                end_amount = sql2["leave_amount"]
                count_amount = start_amount - end_amount
                self.assertEqual(1 ,end_invest - start_invest)
                self.assertEqual(data["amount"],count_amount)
                self.assertEqual(1,end_log - start_log)

            if case_data["title"] == "投资金额等于项目可投金额" :
                sql3 = self.db.find__all("SELECT * FROM future.invest WHERE loan_id = {} and member_id = {}".
                                          format(CaseData.loan_id,CaseData.member_id))
                # sql4 = self.db.find__all("SELECT * FROM future.repayment WHERE invest_id={}".format(sql3["id"]))
                # self.assertTrue(sql4)
                for invest in sql3:
                #     获取当前这条投资记录，生成对应的回款
                    count = self.db.find__count("SELECT * FROM future.repayment WHERE invest_id={}".format(invest["id"]))
                    # 断言查询到的条数的布尔值是否为True(0的布尔值是Flase,只要不是0条，这个断言就会通过)
                    self.assertTrue(count)

        except Exception as e:
            log.error("{}，用例执行不通过".format(case_data["title"]))
            log.exception(e)
            self.excel.write_data(row=row,column=8,value="不通过")
            raise e

        else:
            log.info("{},用例执行通过".format(case_data["title"]))
            self.excel.write_data(row=row,column=8,value="通过")

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

