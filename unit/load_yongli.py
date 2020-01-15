import unittest

suite = unittest.TestSuite()

# 方法一：
# suite.addTest(TestMathMethod("test_add_two_positive"))
# suite.addTest(TestMathMethod("test_add_two_zero"))
# suite.addTest(TestMathMethod("test_add_two_negative"))
# runner = unittest.TextTestRunner()
# runner.run(suite)


# 方法二：

# TestLoader  两种方法，一种根据模块名  ，一种针对类名
import danyuanceshi
loader = unittest.TestLoader()  # 创建一个加载器
#suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
suite.addTest(loader.loadTestsFromModule(danyuanceshi))
with open("test.txt", "w+", encoding="UTF-8") as file:
    runner = unittest.TextTestRunner(stream=file, verbosity=2)
    runner.run(suite)
# from BeautifulReport   import BeautifulReport
# with open("test_report.html", 'wb') as file:
#     runner = BeautifulReport(suite)
#     runner.run(suite)
