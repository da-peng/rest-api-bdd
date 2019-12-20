from behave import *
from utils.base_http import BaseHttp
from features.lancome.steps.const import lancome_url


from_post = BaseHttp().form_post

@Given(u'请求游戏结果判断接口{path}')
def step(context,path):
    context.url = lancome_url+path


@Given('游戏结果判断接口参数{mixNick}&&{gameType}&&{gameUsedSeconds}&&{gamePoint}')
def step_impl(context,mixNick,gameType,gameUsedSeconds,gamePoint):

    request_body= {
        'mixNick':mixNick,
        'gameType':gameType,
        'gameUsedSeconds':gameUsedSeconds,
        'gamePoint':gamePoint
    }
    from_post(request_body,context.url)

