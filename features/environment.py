# encoding=utf-8
from utils.config_parser import config
import os


# 如果环境不同则，则删除持久化文件，这个还未实现

def before_scenario(context, scenario):
    env_dict = os.environ
    env = env_dist.get('TestEnv')
    if env == '':
        env = config['env']['TEST_ENV']

    context.env = env
    if env == 'test':
        service_cap = config['test.service']
        context.host = service_cap['URL']
        context.db_prefix = ''
        context.tenant_code = service_cap['TENANT_CODE']
    elif env == 'uat':
        service_cap = config['uat.service']
        context.host = service_cap['URL']
        context.db_prefix = 'uat_'
        context.tenant_code = service_cap['TENANT_CODE']
    elif env == 'pro':
        service_cap = config['pro.service']
        context.host = service_cap['URL']
        context.db_prefix = ''
        context.tenant_code = service_cap['TENANT_CODE']


def after_step(context, step):
    print()


if __name__== '__main__':
    env_dict = os.environ
    env = env_dist.get('TestEnv')
    if env == '':
        env = config['env']['TEST_ENV']