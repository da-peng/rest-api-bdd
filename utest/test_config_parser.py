# encoding=utf-8

from utils.config_parser import config


class TestConfigParser(object):

    def test(self):
        assert config.sections() is not None
        assert config['test.service']['URL'] == 'https://msa-test-server.meizhidev.com'


