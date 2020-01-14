import requests
import unittest
from test_demo import http_request
from test_demo.http_request import HttpRequest


class TestHttp(unittest.TestCase):

    def setUp(self):
        self.login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        self.login_data = {"mobilephone": 18688773467, "pwd": "123456"}
        self.recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
        self.cookies = HttpRequest().http_request(self.login_data, self.login_data, 'get').cookies

    def test_login_normal(self):  # 正常登陆

        data = {"mobilephone": 18688773467, "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url, data, "get")
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as e:
            print("test_login_normal's error is {}".format(e))

    def test_login_wrong_pwd(self):

        data = {"mobilephone": 18688773467, "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url, data, "post")

    def test_recharge_normal(self):

        data = {"mobilephone": 18688773467, "amount": "123456"}
        res = HttpRequest().http_request(self.recharge_url, data, "post",self.cookies)

    def test_recharge_negative(self):

        data = {"mobilephone": 18688773467, "amount": "-100"}
        res = HttpRequest().http_request(self.recharge_url, data, "post",self.cookies)

    def tearDown(self):
        pass
