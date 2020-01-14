import unittest
from test_demo.test_http import TestHttp
import HTMLTestRunner

test_data = [{"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
              "data": {"mobilephone": 18688773467, "pwd": "123456"}, "expected": "10001", "method": "post"},
             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
              "data": {"mobilephone": 18688773467, "pwd": "123456"}, "expected": "20111", "method": "post"},
             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
              "data": {"mobilephone": 18688773467, "amount": "123456"}, "expected": "10001", "method": "get"},
             {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge",
              "data": {"mobilephone": 18688773467, "amount": "-123456"}, "expected": "20111", "method": "get"

              }]

suite = unittest.TestSuite()
# 通过loader方式加载测试用例
# loader = unittest.TestLoader()
for item in test_data:  # 创建实例

    suite.addTest(TestHttp('test_api', item['url'], item['data'], item['method'], item['expected']))

# 执行
with open("test_summer.html", 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title=None, description=None)
    runner.run(suite)
