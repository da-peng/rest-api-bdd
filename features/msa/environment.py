# encoding=utf-8
from utils.config_parser import config as conf
import os

# 如果环境不同则，则删除持久化文件，这个还未实现
msa_config_path = '/conf/msa/env.ini'

def before_scenario(context, scenario):
    env_dict = os.environ
    env = env_dict.get('TestEnv')
    # 此处需要验证
    config = conf(msa_config_path)
    if env is None:
        env = config['env']['TEST_ENV']
    context.env = env

    for i in ['test','uat','pro']:
        if env == i:
            service_cap = config[i+'.service']
            context.host = service_cap['URL']

def after_step(context, step):
    print()


<<<<<<< HEAD
if __name__== '__main__':
    config = conf(msa_config_path)
    env_dict = os.environ
    env = env_dict.get('TestEnv')
    print(env)
    if env is None:
        print(env)
    env = config['env']['TEST_ENV']
    print(env)
=======
# if __name__== '__main__':
#     env_dict = os.environ
#     env = env_dict.get('TestEnv')
#     print(env)
#     if env is None:
#         print(env)
#         # env = config['env']['TEST_ENV']
>>>>>>> 999a142d923ccf2aacf45149a21ab02f83817c73
