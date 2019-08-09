from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url
import json

from_post = HttpUtils().form_post
from_get = HttpUtils().form_get
GAME_TYPE = 'LITTLE_BLACK_BOTTLE'

@Given(u'{mixNick}获得游戏分数{gamePoint}分')
def step(context,mixNick,gamePoint):
    url = lancome_url+'/nascent/point/onlineadd'
    context.mixNick = mixNick
    print(mixNick)
    request_body= {
        'mixNick':mixNick,
        'gameType':GAME_TYPE,
        'gameUsedSeconds':10,
        'gamePoint':gamePoint
    }
    response = from_post(request_body, url)
    response = json.loads(response.text)
    context.response= response # 传进入断言用

@Then(u'复活前check游戏分数{gamePoint},还差{point}分，得{amount}个加赠券')
def step_impl(context,gamePoint,point,amount):
    url = lancome_url + '/nascent/point/check'
    mixNick = context.mixNick

    request_body= {
        'mixNick':mixNick,
        'gameType':GAME_TYPE,
        'gameUsedSeconds':10,
        'gamePoint':gamePoint
    }
    response = from_post(request_body,url)
    response = json.loads(response.text)
    responseContent= response['responseContent']
    responseContent= json.loads(responseContent)

    points = responseContent['point']
    amounts = responseContent['amount']

    assert points == int(point),'实际：{0}==?预期：{1}'.format(points,point)
    assert amounts == int(amount),'实际：{0}==?预期：{1}'.format(amounts,amount)

@Then(u'本场游戏结束提交数据，游戏分数{gamePoint}分')
def step(context,gamePoint):
    mixNick= context.mixNick
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

    response = json.loads(response.text)
    context.response= response # 传进入断言用

@Then(u'断言获得加赠券{cards}张及今日游戏最高分{gamePoint}')
def step_impl(context,cards,gamePoint):
    url = lancome_url + '/online-game-rankings/my-scores'

    mixNick = context.mixNick
    request_parames = {
        'mixNick': mixNick,
        'gameType': GAME_TYPE
    }

    response = from_get(request_parames, url)
    response = json.loads(response.text)
    cards_ret = response['responseContent'][0]['cards']
    game_point = response['responseContent'][0]['gamePoint']

    assert cards_ret == int(cards),'实际：{0}==?预期：{1}'.format(cards_ret,cards)
    assert game_point == int(gamePoint),'实际：{0}==?预期：{1}'.format(game_point,gamePoint)









