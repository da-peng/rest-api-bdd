from features.lancome.steps.const import lancome_url
from behave import *
from utils.http_util import HttpUtils
from utils.log_manage import Log as log
import json
import time
from_get = HttpUtils().form_get
from_post = HttpUtils().form_post


@Given(u'获取第一名的分数和混淆昵称, 参数{gameType}')
def step(context,  gameType):
    url = lancome_url + '/online-game-rankings/list'

    gameDate =  '20190809'
    # gameDate =time.strftime('%Y%m%d', time.localtime())

    request_params = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    res = from_get(request_params, url)
    res = json.loads(res.text)
    rank_list = res['responseContent']
    if len(rank_list)==0:
        assert False, "排行榜数据为空"
    first = res['responseContent'][0]

    first_mixnick = first['mixNick']
    first_gamePoint = first['gamePoint']

    log.info('第一名的混淆昵称{0}，分数{1}'.format(first_mixnick, first_gamePoint))

    ranking = first["ranking"]

    assert ranking == 1, '不是第一名的数据'

    context.first_gamePoint = first_gamePoint
    context.gameType = gameType



@Then(u'{mixNick}提交游戏结果')
def step_impl(context,mixNick):

    url = lancome_url + '/nascent/point/onlineadd'
    gamePoint = context.first_gamePoint
    gameType = context.gameType
    request_body= {
        'mixNick':mixNick,
        'gameType':gameType,
        'gameUsedSeconds':10,
        'gamePoint':gamePoint
    }
    response=from_post(request_body,url)

    context.mixNick = mixNick


@Then(u'断言变动后的排行榜第一名的信息')
def step(context,):
    url = lancome_url + '/online-game-rankings/list'

    gameDate = time.strftime('%Y%m%d', time.localtime())
    gameType = context.gameType
    request_params = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    res = from_get(request_params, url)
    res = json.loads(res.text)

    first = res['responseContent'][0]

    first_mixnick = first['mixNick']
    first_gamePoint = first['gamePoint']

    log.info('第一名的混淆昵称{0}，分数{1}'.format(first_mixnick, first_gamePoint))

    ranking = first["ranking"]

    assert ranking == 1, '不是第一名的数据'
    assert first_mixnick == context.mixNick , '第一名混淆昵称相同'


