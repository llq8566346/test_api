import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from cases import test_register
from common.handlepath import CASESDIR,REPORTSDIR
from common.handle_email import handle_email
from common.handlepath import REPORTSDIR
import os
# from BeautifulReport import BeautifulReport

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.discover(CASESDIR))


runner = HTMLTestRunner(stream=open("reports/reports2.html", "wb"),
                        title = "林亮钦的第二次测试报告",
                        description= "第二次测试报告",
                        tester = "林亮钦")

runner.run(suite)

filename = os.path.join(REPORTSDIR,"reports2.html")

handle_email(filename,"林亮钦的测试报告最终版")

# br = BeautifulReport(suite)
#
# br.report("前程贷项目用例",filename="report1.html",report_dir=REPORTSDIR)



           





