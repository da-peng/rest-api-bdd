# encoding=utf-8
from utils.config_parser import config as conf
import os

lancome_conf_path = '/conf/lppz-xxl/env.ini'
# 如果环境不同则，则删除持久化文件，这个还未实现

def before_scenario(context, scenario):
    env_dict = os.environ
    env = env_dict.get('TestEnv') # 环境变量
    # 此处需要验证
    config = conf(lancome_conf_path)
    if env is None:
        env = config['env']['TEST_ENV']
    context.env = env
    service_cap = ''
    if env == 'test':
        service_cap = config['test.service']
    elif env == 'uat':
        service_cap = config['uat.service']
    elif env == 'pro':
        service_cap = config['pro.service']

    context.host = service_cap['host'.upper()]
    context.tenant_code = service_cap['tenant_code'.upper()]
    context.headers={'token':service_cap['token'.upper()]}


def after_step(context, step):
    print()

