# 接口测试的本质就是测试类里面的函数，通过数据驱动

# 单元测试的本质 是测试函数（代码级别）
# 单元测试框架  unittest+接口  pytest+web-->接口

# pytest+jenkins+allure

# 写用例  TestCase
# 执行用例   TestSuite 存储用例    TESTLoader 找用例，加载用例 存储到TESTSuite中
# 对比期望结果，实际结果   断言 Assert
# 出具测试报告   HTMLTestRunner


from math_method import MathMethod
import unittest


# 写一个测试类 ，对我们自己写的math method模块里面的类进行单元测试
class TestMathMethod(unittest.TestCase):  # 继承testcase来编写测试用例

    """对自己写的数学方法进行测试"""

    # 编写测试用例
    # 一个用例就是一个函数，不能传递参数 只有self关键字

    def test_add_two_positive(self):
        """两个正数相加"""
        res = MathMethod(1, 1).add()
        print("1+1的结果是：", res)
        # 加一个断言判断期望值与预期结果  一致通过，不一致失败
        self.assertEqual(2, res)

    def test_add_two_zero(self):
        """两个0相加"""
        res = MathMethod(0, 0).add()
        print("0+0的结果是", res)
        self.assertEqual(1, res)

    def test_add_two_negative(self):
        """两个负数相加"""
        res = MathMethod(-1, -2).add()
        print("-1+-2的结果是：", res)
        self.assertEqual(-3, res)


class TestMulti(unittest.TestCase):  # 继承testcase来编写测试用例

    """对自己写的数学方法进行测试"""

    # 编写测试用例
    # 一个用例就是一个函数，不能传递参数 只有self关键字

    def test_multi_two_positive(self):
        """两个正数相乘"""
        res = MathMethod(1, 1).multi()
        print("1*1的结果是：", res)

    def test_multi_two_zero(self):
        """两个0相加"""
        res = MathMethod(0, 0).multi()
        print("0*0的结果是", res)

    def test_multi_two_negative(self):
        """两个负数相加"""
        res = MathMethod(-1, -2).multi()
        print("-1*-2的结果是：", res)


if __name__ == '__main__':
    unittest.main()
