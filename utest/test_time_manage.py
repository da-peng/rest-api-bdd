# encoding=utf-8
from utils.time_manage import *
import pytest
import allure
@allure.feature('日期时间操作')
class TestTimeManage(object):

    @allure.story('当前北京时间（东八区）')
    def test_getCurrentTime(self):
        assert getCurrentTime() is not  None

    @allure.story('当前时间后1个小时')
    def test_getEndTime(self):
        assert getEndTime() is not None
        assert get_time_stamp() is not None
