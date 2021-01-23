# -*- coding: utf-8 -*- 
# @Time    : 2021/1/7 3:17 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : apiMethod.py
# @Software: PyCharm


import requests
import json


class RunMain:
    def send_post(self, url, data):
        result = requests.post(url, data=data)
        return result

    def send_get(self, url, data):
        result = requests.get(url, params=data)
        return result

    def run_main(self, method, url=None, data=None):
        result = None
        if method == "get" or method == "GET":
            result = self.send_get(url, data)
        elif method == "post" or method == "POST":
            result = self.send_post(url, data)
        else:
            print("请求错误，请检查")
        return result


# if __name__ == '__main__':
#     try:
#         url = "http://zx.1daas.com/api/member/login"
#         data = {
#             "name": "18857292945",
#             "password": "c4389ffffe6ae7ffee519fafd7bcc03b18ced6f6",
#             "platform": "2"
#         }
#         data_str = json.dumps(data)
#         run = RunMain()
#         res = run.run_main("post", url, data_str)
#         print(res.status_code)
#         print(res.json())
#     except Exception as e:
#         print(e)
