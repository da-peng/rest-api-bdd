# encoding=utf-8

from utils.config_parser import config
import pytest
import allure
# 结合allure输出报告
@allure.feature('配置')
class TestConfigParser(object):

    @allure.story('配置读取')
    def test(self):
        assert config.sections() is not None
        assert config['test.service']['URL'] == 'https://msa-test-server.meizhidev.com'


