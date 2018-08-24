# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from API_automation.common.logger import MyLog
import API_automation.config.readConfig as readConfig
from API_automation.common.configEmail import MyEmail
import os

localReadConfig = readConfig.ReadConfig()


class AllTest(object):

        def __init__(self):
            global on_off, logger, resultPath
            self.caseList = []
            self.caselistFile = os.path.join(readConfig.proDir, "caselist.txt")
            self.case_file = os.path.join(readConfig.project_path, "testCase")
            # self.resultPath = os.path.join(readConfig.project_path, "test_report")
            self.email = MyEmail.get_email()
            log = MyLog.get_log()
            logger = log.get_logger()
            resultPath = log.get_report_path()
            on_off = localReadConfig.get_email("on_off")

        def set_case_list(self):
            fb = open(self.caselistFile, 'r+', encoding='utf-8')
            for value in fb.readlines():
                data = str(value)
                if data != '' and not data.startswith("#"):
                    self.caseList.append(data.replace("\n", ""))
            fb.close()

        def set_case_suite(self):
            self.set_case_list()
            test_suite = unittest.TestSuite()
            suite_model = []

            for case in self.caseList:
                case_name = case.split("/")[-1]
                print(case_name+".py")
                discover = unittest.defaultTestLoader.discover(self.case_file, pattern=case_name + '.py',
                                                               top_level_dir=None)
                suite_model.append(discover)

            if len(suite_model) > 0:
                for suite in suite_model:
                    for test_name in suite:
                        test_suite.addTest(test_name)
            else:
                return None
            return test_suite

        def run(self):
            global fp
            try:
                suit = self.set_case_suite()
                if suit is not None:
                    logger.info("********TEST START********")
                    fp = open(resultPath, 'wb')
                    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"web-login项目测试报告",
                                                           description=u"用例测试情况")
                    runner.run(suit)
                    fp.flush()
                else:
                    logger.info("Have no case to test.")
            except Exception as ex:
                logger.error(str(ex))
            finally:
                fp.close()
                logger.info("*********TEST END*********")
                # send test report by email
                if on_off == 'on':
                    self.email.send_email()
                elif on_off == 'off':
                    logger.info("Doesn't send report email to developer.")
                else:
                    logger.info("UnKnow state.")

if __name__ == '__main__':
    obj = AllTest()
    obj.run()
