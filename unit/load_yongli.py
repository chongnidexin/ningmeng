from danyuanceshi import TestMathMethod
import unittest

suite = unittest.TestSuite()

# 方法一：
# suite.addTest(TestMathMethod("test_add_two_positive"))
# suite.addTest(TestMathMethod("test_add_two_zero"))
# suite.addTest(TestMathMethod("test_add_two_negative"))
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 方法二：
import danyuanceshi
import HtmlTestRunner
# TestLoader  两种方法，一种根据模块名  ，一种针对类名
# loader = unittest.TestLoader()  # 创建一个加载器
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
# suite.addTest(loader.loadTestsFromModule(danyuanceshi))
# with open("test.txt", "w+", encoding="UTF-8") as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)
#     runner.run(suite)

with open("test_report.html", 'wb') as file:
    runner = HtmlTestRunner.HTMLTestRunner( stream=file, output="./reports/", verbosity=2, report_title="首次测试报告", descriptions=True, failfast=False, buffer=False,
                  report_name=None, template=None, resultclass=None,
                 add_timestamp=True, open_in_browser=False,
                 combine_reports=False, template_args=None)
    runner.run(suite)