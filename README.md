# Apitest
##python + requests + pytest + allure

#pytest启动命令
pytest 测试用例路径::测试类::测试方法

`pytest testcase/test_login.py::TestLogin::test_cart_list`

#allure命令
*执行完成后，在当前目录下生成report目录，report目录下生成一个allure_raw的目录，这里存放了测试报告的JSON格式原始文件，不能打开成html的报告  
*--alluredir=DIR 指定报告的目录路径  
*--clean-alluredir 如果已经存在报告，就先清空它  
*--allure-no-capture 不加载 logging/stdout/stderr 文件到报告

`pytest --alluredir ./report --clean-alluredir`

启动allure报告服务，输入生成的IP地址和端口即可访问

`allure serve report`
