# encoding=utf-8
from utils.config_parser import config

common_config_path = '/conf/common/env.ini'

config = config(common_config_path)

level = config['log.level']['level']


class Log(object):

    def __init__(self):
        pass

    @staticmethod
    def info(msg):
        if level in ['info', 'debug']:
            print('INFO:' + '* ' * 3 + msg + ' *' * 3)

    @staticmethod
    def debug(msg):
        if level in ['debug']:
            print('DEBUG:' + '* ' * 3 + msg + ' *' * 3)

    @staticmethod
    def error(msg):
        if level in ['debug', 'error']:
            print('ERROR:' + '* ' * 3 + msg + ' *' * 3)
