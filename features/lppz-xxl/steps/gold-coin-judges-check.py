from behave import *
import re


@Given(u'访问判断是否获得过相关游戏接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)

