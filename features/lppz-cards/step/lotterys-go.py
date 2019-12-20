from behave import *
from utils.base_http import BaseHttp
import re

post = BaseHttp().post


@Given(u'访问抽卡接口{path}，混淆昵称{mixNick}')
def step(context, path, mixNick):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)

    url = context.path
    requset_params = {
        'mixNick': mixNick
    }
    response = post(requset_params, url, context.headers)
    context.statusCode = response['statusCode']

