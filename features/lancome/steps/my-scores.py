from behave import *
from utils.base_http import BaseHttp
from features.lancome.steps.const import lancome_url


from_get = BaseHttp().form_get

@Given(u'请求我的游戏成绩接口{path}')
def step(context,path):
    context.url = lancome_url+path


@Given('我的游戏成绩接口参数{mixNick}&&{gameType}')
def step_impl(context,mixNick,gameType):

    request_parames= {
        'mixNick':mixNick,
        'gameType':gameType
    }
    from_get(request_parames,context.url)