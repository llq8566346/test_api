
import os

from common.handlepath import LOGDIR

import logging

from common.handleconfig import conf

class HandleLog(object):

    @staticmethod
    def create_logger():

        mylog = logging.getLogger()

        mylog.setLevel(conf.get("log","mylog_level"))

        sh = logging.StreamHandler()

        sh.setLevel(conf.get("log","sh_level"))

        fh = logging.FileHandler(filename=os.path.join(LOGDIR,"mylog.log"), encoding="utf-8")

        fh.setLevel(conf.get("log","fh_level"))

        fm = logging.Formatter("%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s")

        fh.setFormatter(fm)

        sh.setFormatter(fm)

        mylog.addHandler(fh)

        mylog.addHandler(sh)

        return mylog


log = HandleLog.create_logger()









