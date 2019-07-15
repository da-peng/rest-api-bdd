# encoding=utf-8
from utils.file_manage import *
import allure

@allure.feature('文件操作')
class TestFileManage(object):

    @allure.story('文件读取')
    def test_read(self):
        assert  read() is not None

    @allure.story('文件末尾添加')
    def test_add(self):
        assert add({'a':'1'}) is None

    @allure.story('文件覆盖写入')
    def test_write(self):
        assert  write('a') is None