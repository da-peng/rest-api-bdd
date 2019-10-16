from behave import *
from utils.http_util import HttpUtils
import re

formpost = HttpUtils().form_postBytoken


@Given(u'访问抽奖接口{path}，混淆昵称{mixNick}')
def step(context, path, mixNick):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)

    url = context.path
    requset_params = {
        'mixNick': mixNick
    }
    response = formpost(requset_params, url, context.token)
    context.statusCode = response['statusCode']


@Then(u'断言接口访问成功')
def step(context):
    assert context.statusCode == '20000', '接口访问失败'
