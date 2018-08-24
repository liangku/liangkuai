import API_automation.config.readConfig as readConfig
import os
from xlrd import open_workbook
from API_automation.common.logger import MyLog as Log

localReadConfig = readConfig.ReadConfig()
xls_Path = os.path.dirname(os.path.abspath('./..'))
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


def get_xls(xls_name, sheet_name):
    """
    从excel文件中读取测试用例
    :param xls_name: 
    :param sheet_name: 
    :return: 
    """
    cls = []
    # 获取xls文件地址
    xlsPath = os.path.join(xls_Path, "testFile", xls_name)
    # 打开xls文件
    file = open_workbook(xlsPath)
    # 获取表格名称
    sheet = file.sheet_by_name(sheet_name)
    # 获取表格的一行
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls
