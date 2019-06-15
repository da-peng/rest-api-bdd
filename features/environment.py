#encoding=utf-8
from utils.config_parser import config

def before_scenario(context, scenario):
    context.host = config['uat.service.url']['URL']


def after_step(context, step):
    print()