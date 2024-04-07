# from configparser import ConfigParser
#
# config = ConfigParser()
#
# config.read("conf/conf.ini",encoding="utf-8")
#
# res = config.sections()
#
# print(res)
#
# res  = config.get("log","level")
#
# print(res)
#
# config.set("log" , "name","123")
#
# config.write(fp=open("conf/conf.ini","w"))

from configparser import ConfigParser
import os
from common.handlepath import CONFDIR


class handleconfig(ConfigParser):

    def __init__(self,filename):
        super().__init__()
        self.filename = filename
        self.read(filename , encoding="UTF-8")

    def conf_write(self,section,option,value):
        self.set(section,option,value)
        self.write(fp=open(self.filename,"w"))


conf = handleconfig(os.path.join(CONFDIR,"conf.ini"))














