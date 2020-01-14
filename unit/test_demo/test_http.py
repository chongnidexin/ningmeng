import requests
import unittest

from test_demo.http_request import HttpRequest
from test_demo.get_data import GetData


class TestHttp(unittest.TestCase):

    def __init__(self, methodName, url, data, method, expected):  # 通过初始化函数来传递参数
        super(TestHttp, self).__init__(methodName)  # 父类的方法保留了
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected

    def setUp(self):
        # self.login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        # self.login_data = {"mobilephone": 18688773467, "pwd": "123456"}
        # self.recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
        # self.cookies = HttpRequest().http_request(self.login_data, self.login_data, 'get').cookies
        pass

    def test_api(self):  # 正常登陆

        # data = {"mobilephone": 18688773467, "pwd": "123456"}
        res = HttpRequest().http_request(self.url, self.data, self.method, getattr(GetData, 'Cookie'))
        if res.cookies:
            setattr(GetData, 'Cookie', res.cookies)
        try:
            self.assertEqual('10001', res.json()['code'])
        except AssertionError as e:
            print("test_login_normal's error is {}".format(e))
            raise e

    # def test_login_wrong_pwd(self):
    #
    #     data = {"mobilephone": 18688773467, "pwd": "123456"}
    #     res = HttpRequest().http_request(self.login_url, data, "post")
    #
    # def test_recharge_normal(self):
    #
    #     data = {"mobilephone": 18688773467, "amount": "123456"}
    #     res = HttpRequest().http_request(self.recharge_url, data, "post", self.cookies)
    #
    # def test_recharge_negative(self):
    #
    #     data = {"mobilephone": 18688773467, "amount": "-100"}
    #     res = HttpRequest().http_request(self.recharge_url, data, "post", self.cookies)

    def tearDown(self):
        pass
