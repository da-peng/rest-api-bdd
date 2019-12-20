from behave import *
from utils.base_http import BaseHttp
import re

post = BaseHttp().post


@Given(u'访问抽卡接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入混淆昵称{mixNick}游戏关卡{gameLevel}游戏关卡{gameScore}')
def step(context,mixNick,gameLevel,gameScore):
    url = context.path
    requset_params = {
        'mixNick': mixNick,
        'gameLevel':int(gameLevel),
        'gameScore':int(gameScore)
    }
    response = post(requset_params, url, context.headers)
    context.statusCode = response['statusCode']