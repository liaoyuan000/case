import unittest
from HTMLTestRunner import HTMLTestRunner


class TestA(unittest.TestCase):
    def setUp(self):
        print("setup方法执行了")

    def tearDown(self):
        print("teardown方法执行了")

    def test01(self):
        print("haha")

    def test02(self):
        print("hehe")


if __name__ == '__main__':
    unittest.main()
    suite = unittest.defaultTestLoader.discover("./",pattern="iwebshop_test*")
    # runner= unittest.TextTestRunner()
    # runner.run(suite)
    # 这里必须是“wb”
    with open("./report.html", "wb") as f:
        # 用HTMLTestRunner这个py文件生成runner对象
        runner = HTMLTestRunner(stream=f, description="测试用例一共6涛")
        # 文件路径如下
        runner.run(suite)
