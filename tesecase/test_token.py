# -*- coding: utf-8 -*- 
# @Time    : 2021/1/7 3:05 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : test_token.py
# @Software: PyCharm


import pytest
import requests
import json

url = "http://zx.1daas.com/api"


def test_get_token():
    data = {
        "name": "18857292945",
        "password": "c4389ffffe6ae7ffee519fafd7bcc03b18ced6f6",
        "platform": "2"
    }
    res = requests.post(url + "/member/login", data)
    print(res.status_code)
    print(res.json())
    assert res.status_code == 200


test_get_token()
