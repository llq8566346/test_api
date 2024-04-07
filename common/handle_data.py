import re
from common.handleconfig import conf

class CaseData():
    pass

def replace_data(s):
    r = r"#(.*?)#"

    while re.search(r,s):
        res = re.search(r,s)
        data = res.group()
        key = res.group(1)

        try:
            s = s.replace(data,conf.get("test_data",key))

        except Exception:
            s = s.replace(data,str(getattr(CaseData,key)))

    return s




#
# if __name__ == '__main__':
# s = "123#member_id#111111"
# res = Casedata.replace_data(s)
# print(res)






