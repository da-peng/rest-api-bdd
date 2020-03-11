# encoding=utf-8
from utils.config_parser import config

common_config_path = '/conf/common/env.ini'

config = config(common_config_path)

level_conf = config['log.level']['level']


class Log(object):

    def __init__(self):
        pass

    @classmethod
    def is_enable(cls, level):
        levels = ['debug', 'info', 'warn', 'error']
        if level in levels:
            return levels.index(level) >= levels.index(level_conf)
        else:
            return False

    @classmethod
    def info(cls, msg):
        if cls.is_enable('info'):
            print('INFO:' + '* ' * 3 + msg + ' *' * 3)

    @classmethod
    def debug(cls, msg):
        if cls.is_enable('debug'):
            print('DEBUG:' + '* ' * 3 + msg + ' *' * 3)

    @classmethod
    def error(cls, msg):
        if cls.is_enable('error'):
            print('ERROR:' + '* ' * 3 + msg + ' *' * 3)


if __name__ == "__main__":
    # a = 10
    # # 1010
    #
    # print(bin(a))
    # print(oct(a))
    # print(hex(a))
    # print(eval(hex(a)))
    # # ~：逐位取反  0011
    # print(bin(~7))
    # print(~1)
    # print(~2)
    # print(~3)
    # print(~4)
    # a = 110
    # a &= ~7
    g = lambda x : x&~7
    # 104
    print(g(110))
    # 96
    print(g(100))
    # 8
    print(g(10))