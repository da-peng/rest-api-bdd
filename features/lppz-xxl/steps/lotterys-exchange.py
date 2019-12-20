from behave import *
from utils.base_http import BaseHttp
import re
 
post = BaseHttp().post


@Given(u'访问兑奖接口{path}，输入混淆昵称{mixNick}&奖品类型{type}&奖品记录ID{prizeId}')
def step(context, path, mixNick,type,prizeId):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)
    request_body = {
        'mixNick': mixNick,
        'type':type,
        'prizeId':prizeId
    }
    response = post(request_body, context.path, context.headers)
    context.statusCode = response['statusCode']

