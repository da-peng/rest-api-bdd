from behave import *
import re


@Given(u'访问获取游戏机会数量接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)

