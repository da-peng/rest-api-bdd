from behave import *
from utils.base_http import BaseHttp
import re

post = BaseHttp().post


@Given(u'访问赚取游戏机会接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入任务类型{sourceType}&混淆昵称{mixNick}&新年祝福{wellWishing}')
def step(context, sourceType, mixNick,wellWishing):
    url = context.path

    a = {'wellWishing': wellWishing} if sourceType == 'WELL_WISHING' else {}

    request_body = {
        'sourceType': sourceType,
        'mixNick': mixNick,
        # 新年祝福，sourceType=WELL_WISHING时必需
        **a
    }
    response = post(request_body, url, context.headers)
    context.statusCode = response['statusCode']
