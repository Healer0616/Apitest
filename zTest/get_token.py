# -*- coding: utf-8 -*- 
# @Time    : 2021/1/5 9:44 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : get_token.py
# @Software: PyCharm

import requests
import json


# url = "http://zx.1daas.com/api/member/login"
# params = {
#     "name": "18857292945",
#     "password": "c4389ffffe6ae7ffee519fafd7bcc03b18ced6f6",
#     "platform": "2"
# }
# header = {}
# res = requests.post(url, json=params)
# print(res.json())
# print(res.json()['data']["token"])

# 获取token
def get_token(inbodyData):
    """
    :url:接口地址
    :data:请求参数
    :return: 返回token
    """
    url = "http://zx.1daas.com/api/member/login"
    bodyData = json.loads(inbodyData)
    data = bodyData
    res = requests.post(url, json=data)
    # return res.json()['data']["token"]
    return res.json()


# 获取用户信息
def get_member_info():
    url = "http://zx.1daas.com/api/member/info"
    params = {
        "token": get_token()
    }
    header = {'Content-Type': 'application/json', "token": get_token()}
    res1 = requests.get(url, params=params, headers=header)
    return res1.json()

    # print(res1.request.headers)

    # 断言判断
    # if res1.json()['data']["name"] == "Ha":
    #     print(f"接口pass，总共耗时{res1.elapsed.total_seconds()}s")
    # else:
    #     print(f"接口fail，总共耗时{res1.elapsed.total_seconds()}s")
