from behave import *
from utils.http_util import HttpUtils
import re

formget = HttpUtils().form_getBytoken


@Given(u'访问点赞排行接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入获取条数{limit}')
def step(context, limit):
    url = context.path
    requset_params = {
        'limit': limit
    }
    response = formget(requset_params, url, context.token)
    context.statusCode = response['statusCode']


@Then(u'断言点赞排行接口访问成功')
def step(context):
    assert context.statusCode == '20000', '点赞排行接口访问失败'
