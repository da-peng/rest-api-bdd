from behave import *
from utils.http_util import HttpUtils
import re

formget = HttpUtils().form_getBytoken


@Given(u'访问获取幸运值接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@Then(u'断言获取幸运值成功')
def step(context):
    assert context.statusCode == '20000', '接口访问失败'
