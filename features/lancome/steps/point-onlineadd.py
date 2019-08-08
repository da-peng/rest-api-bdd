from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url


from_post = HttpUtils().form_post

@Given(u'请求游戏结束调用积分接口{path}')
def step(context,path):
    context.url = lancome_url+path


@Given('游戏结束调用积分接口参数{mixNick}&&{gameType}&&{gameUsedSeconds}&&{gamePoint}')
def step_impl(context,mixNick,gameType,gameUsedSeconds,gamePoint):

    request_body= {
        'mixNick':mixNick,
        'gameType':gameType,
        'gameUsedSeconds':gameUsedSeconds,
        'gamePoint':gamePoint
    }
    from_post(request_body,context.url)

