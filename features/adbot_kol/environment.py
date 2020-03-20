# encoding=utf-8
from utils.config_parser import config as conf
from utils.file_manage import *
from features.adbot_kol.utils.token_manager import getLoginInfo

lancome_conf_path = '/conf/adbot-bj/env.ini'


# 如果环境不同则，则删除持久化文件，这个还未实现

def before_scenario(context, scenario):
    env_dict = os.environ
    env = env_dict.get('TestEnv')
    # 此处需要验证
    config = conf(lancome_conf_path)
    if env is None:
        env = config['env']['TEST_ENV']
    context.env = env
    if env == 'test':
        service_cap = config['test.service']
    elif env == 'uat':
        service_cap = config['uat.service']
    elif env == 'pro':
        service_cap = config['pro.service']
    context.host = service_cap['URL']
    context.tenant_code = service_cap['TENANT_CODE']
    token = getLoginInfo('token')
    context.headers = {'token': token}


def after_step(context, step):
    print()

if __name__== '__main__':
    print(getLoginInfo('token'))
#     env_dict = os.environ
#     env = env_dict.get('TestEnv')
#     print(env)
#     if env is None:
#         print(env)
#         # env = config['env']['TEST_ENV']
