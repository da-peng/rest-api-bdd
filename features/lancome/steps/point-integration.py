from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url


from_post = HttpUtils().form_post
from_get = HttpUtils().form_get
GAME_TYPE = 'LITTLE_BLACK_BOTTLE'
@Given(u'{mixNick}获得游戏分数{gamePoint}分')
def step(context,mixNick,gamePoint):
    url = lancome_url+'/nascent/point/onlineadd'
    context.mixNick = mixNick
    context.gamePoint = gamePoint
    request_body= {
        'mixNick':mixNick,
        'gameType':GAME_TYPE,
        'gameUsedSeconds':10,
        'gamePoint':gamePoint
    }
    response = from_post(request_body, url)



@Then(u'断言获得加赠券{cards}张及今日游戏最高分{gamePoint}')
def step_impl(context,cards,gamePoint):
    url = lancome_url + '/online-game-rankings/my-scores'

    mixNick = context.mixNick
    request_parames = {
        'mixNick': mixNick,
        'gameType': GAME_TYPE
    }

    response = from_get(request_parames, url)

    cards_ret = response['responseContent']['cards']
    game_point = response['responseContent']['gamePoint']
    assert cards_ret == int(cards)
    assert game_point == int(gamePoint)



@Then(u'断言还差{point}分，得到{amount}个加赠券')
def step_impl(context,point,amount):
    url = lancome_url + '/nascent/point/check'
    mixNick = context.mixNick
    gamePoint = context.gamePoint

    request_body= {
        'mixNick':mixNick,
        'gameType':GAME_TYPE,
        'gameUsedSeconds':10,
        'gamePoint':gamePoint
    }
    response = from_post(request_body,url)
    points = response['responseContent']['point']
    amounts = response['responseContent']['amount']
    assert points == int(point)
    assert amounts == int(amount)





