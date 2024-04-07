
import openpyxl
# import os
# from common.handlepath import DATADIR


class Readexcel(object):

    def __init__(self,filename,sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        self.open()
        data = list(self.sh.rows)
        title = [i.value for i in data[0]]
        cases = []
        for i in data[1:]:
            values = [c.value for c in i]
            case = dict(zip(title,values))
            cases.append(case)

        return cases

    def write_data(self,row,column,value):
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.filename)







# excel = Readexcel(os.path.join(DATADIR,"cases.xlsx"), "audit")
# case_datas = excel.read_data()
# print(case_datas)


