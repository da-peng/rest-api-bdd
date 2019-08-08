from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url

from_get = HttpUtils().form_get

@Given(u'请求获取奖励凭证接口{path}')
def step(context,path):
    context.url = lancome_url+path


@Given('获取奖励凭证接口参数{mixNick}&&{gameType}')
def step_impl(context,mixNick,gameType):

    request_parames= {
        'mixNick':mixNick,
        'gameType':gameType
    }
    from_get(request_parames,context.url)

