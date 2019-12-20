from behave import *
from utils.base_http import BaseHttp
import re

get = BaseHttp().get


@Given(u'访问获取我的集卡接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'请输入混淆昵称{mixNick}')
def step(context, mixNick):
    url = context.path

    request_body = {
        'mixNick': mixNick
    }
    response = get(request_body, url, context.headers)
    context.statusCode = response['statusCode']

