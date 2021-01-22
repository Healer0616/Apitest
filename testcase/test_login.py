# -*- coding: utf-8 -*- 
# @Time    : 2021/1/9 10:29 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : test_login.py
# @Software: PyCharm

import json
from zTest.logger import Logger
from zTest.apiMethod import RunMain




class TestLogin:
    def setup(self):
        self.host = "http://zx.1daas.com/api"
        self.logger = Logger()

    def test_login(self):
        """
        获取登录token
        :return:
        """
        url = self.host + "/member/login"
        data = {
            "name": "18857292945",
            "password": "c4389ffffe6ae7ffee519fafd7bcc03b18ced6f6",
            "platform": "2"
        }
        data_str = json.dumps(data)
        res = RunMain().run_main("post", url, data_str)
        assert res.status_code == 200
        assert res.json()["error"] == ""
        return res.json()["data"]["token"]

    def test_get_info(self):
        """
        获取用户信息
        :return:
        """
        url = self.host + "/member/info"
        data = {
            "token": self.test_login()
        }
        res = RunMain().run_main("get", url, data)
        # print(res.json())
        assert res.status_code == 200
        assert res.json()["data"]["name"] == "Ha"

    # test_get_info()

    def test_goods_list(self):
        """
        商品列表
        :return:
        """
        url = self.host + "/goods/list"
        data = {
            "shopid": 4,
            "from": 1,
            "limit": 10
        }
        res = RunMain().run_main("get", url, data)
        # print(res.json())
        assert res.json()["data"]["goods"][0]["shopid"] == data["shopid"]
        return res.json()["data"]["goods"][4]["goodsid"]

    # goods_list()

    def test_cart_add(self):
        """
        加入购物车
        :return:
        """
        url = self.host + "/cart/add"
        data = {
            "goodsid": self.test_goods_list(),
            "token": self.test_login(),
            "count": 1
        }
        data_str = json.dumps(data)
        res = RunMain().run_main("post", url, data_str)
        # print(res.json())
        assert res.json()["error"] == ""
        return data

    # cart_add()

    def test_cart_list(self):
        """
        购物车列表
        :return:
        """
        url = self.host + "/cart/list"
        data = {
            "token": self.test_login()
        }
        res = RunMain().run_main("get", url, data)
        assert res.status_code == 200
        self.logger.get_log().debug(res)
        # print("token:"+test_login())
        # print("goodsid:"+str(test_cart_add()["goodsid"]))
        print(res.json())
        # print(res.json()["data"]["cartlist"])
        # assert test_cart_add()["goodsid"] in res.json()["data"]["cartlist"]

# if __name__ == '__main__':
#     login = TestLogin()
