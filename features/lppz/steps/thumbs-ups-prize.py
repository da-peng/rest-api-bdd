from behave import *
import re

@Given(u'访问获奖集赞接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)

@Then(u'断言获取集赞奖品成功')
def step(context):
    assert context.statusCode == '20000', '获取集赞奖品失败'