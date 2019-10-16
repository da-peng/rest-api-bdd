#encoding=utf-8
from  configparser import  ConfigParser as conf
import os

current_dir = os.path.dirname(os.path.dirname(__file__))


def config(path):
    config = conf()
    # path= current_dir+'/conf/msa/env.ini'
    absolute_path = current_dir + path
    # print(absolute_path)
    config.read(absolute_path)
    return config



if __name__ == '__main__':
    common_config_path = '/conf/common/env.ini'
    #common_config_path='/conf/lancome/env.ini'

    config = config(common_config_path)

    #level = config['log.level']['level']
    #url=config['test.service']['URL']
    print(config.sections())
    print(config.options('log.level'))


