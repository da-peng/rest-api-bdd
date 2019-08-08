#encoding=utf-8
from  configparser import  ConfigParser as conf
import os

config = conf()

current_dir = os.path.dirname(os.path.dirname(__file__))

path= current_dir+'/conf/msa/env.ini'

config.read(path)

if __name__ == '__main__':
    print(config.sections())

    print(config['test.service.url'])

    for key in config['bitbucket.org']:
        print(key)