# encoding=utf-8
from utils.config_parser import config

common_config_path = '/conf/common/env.ini'

config = config(common_config_path)

level_conf = config['log.level']['level']


class Log(object):

    def __init__(self):
        pass

    @classmethod
    def is_enable(cls,level):
        levels = ['debug', 'info', 'warn', 'error']
        if level in level:
            return levels.index(level) >= levels.index(level_conf)
        else:
            return False

    @classmethod
    def info(cls,msg):
        if cls.is_enable('info'):
            print('INFO:' + '* ' * 3 + msg + ' *' * 3)

    @classmethod
    def debug(cls,msg):
        if cls.is_enable('debug'):
            print('DEBUG:' + '* ' * 3 + msg + ' *' * 3)

    @classmethod
    def error(cls,msg):
        if cls.is_enable('error'):
            print('ERROR:' + '* ' * 3 + msg + ' *' * 3)
