from behave import *
from utils.base_http import BaseHttp
import re

get = BaseHttp().get


@Given(u'访问开始游戏接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)
