from behave import *
from utils.base_http import BaseHttp
import re

post = BaseHttp().post


@Given(u'访问赚取抽卡机会接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入任务类型{sourceType}&混淆昵称{mixNick}')
def step(context, sourceType,  mixNick):
    url = context.path

    request_body = {
        'sourceType': sourceType,
        'mixNick': mixNick
    }
    response = post(request_body, url, context.headers)
    context.statusCode = response['statusCode']
