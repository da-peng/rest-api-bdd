from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url


from_post = HttpUtils().form_post
from_get = HttpUtils().form_get
GAME_TYPE = 'LITTLE_BLACK_BOTTLE'
@Given(u'{mixNick}获得游戏分数{gamePoint}分')
def step(context,mixNick,gamePoint):
    url = lancome_url+'/nascent/point/onlineadd'

    request_body= {
        'mixNick':mixNick,
        'gameType':GAME_TYPE,
        'gameUsedSeconds':10,
        'gamePoint':gamePoint
    }
    from_post(request_body, url)


@Then(u'断言{mixNick}获得加赠券{cards}张及今日游戏最高分{gamePoint}')
def step_impl(context,mixNick,cards,gamePoint):
    url = lancome_url + '/online-game-rankings/my-scores'

    request_parames = {
        'mixNick': mixNick,
        'gameType': GAME_TYPE
    }

    response = from_get(request_parames, url)

    cards_ret = response['responseContent']['cards']
    game_point = response['responseContent']['gamePoint']
    assert cards_ret == int(cards)
    assert game_point == int(gamePoint)



