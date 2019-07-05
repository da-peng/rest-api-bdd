# encoding=utf-8
from utils.config_parser import config


def before_scenario(context, scenario):
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
