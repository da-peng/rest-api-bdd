from behave import *
from utils.base_http import BaseHttp
from features.lancome.steps.const import lancome_url

from_get = BaseHttp().form_get
@Given(u'请求游戏排名接口{path}')
def step(context,path):
    context.url= lancome_url+path

@Given('游戏排名接口参数{gameDate}&{gameType}')
def step(context,gameDate,gameType):

    request_parames = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    r=from_get(request_parames, context.url)



