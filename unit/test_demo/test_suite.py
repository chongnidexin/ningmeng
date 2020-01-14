import unittest
from test_demo import test_http
import HTMLTestRunner

suite = unittest.TestCase()
# 通过loader方式加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_http))

# 执行
with open("test_summer.html", 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title=None, description=None)
    runner.run(suite)
