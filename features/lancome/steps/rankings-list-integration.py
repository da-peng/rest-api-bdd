from features.lancome.steps.const import lancome_url
from behave import *
from utils.http_util import HttpUtils
from utils.log_manage import Log as log
import time

from_get = HttpUtils().form_get
from_post = HttpUtils().form_post


@Given(u'获取第一名的分数和混淆昵称, 参数{gameType}')
def step(context, gameType):
    url = lancome_url + '/online-game-rankings/list'

    gameDate = time.strftime('%Y%m%d', time.localtime())

    request_params = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    res = from_get(request_params, url)
    rank_list = res['responseContent']
    if len(rank_list) == 0:
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
def step_impl(context, mixNick):
    url = lancome_url + '/nascent/point/onlineadd'
    gamePoint = context.first_gamePoint+1
    gameType = context.gameType
    request_body = {
        'mixNick': mixNick,
        'gameType': gameType,
        'gameUsedSeconds': 10,
        'gamePoint': gamePoint
    }
    response = from_post(request_body, url)

    context.mixNick = mixNick


@Then(u'断言变动后的排行榜第一名的信息')
def step(context, ):
    url = lancome_url + '/online-game-rankings/list'

    gameDate = time.strftime('%Y%m%d', time.localtime())
    gameType = context.gameType
    request_params = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    res = from_get(request_params, url)

    first = res['responseContent'][0]

    first_mixnick = first['mixNick']
    first_gamePoint = first['gamePoint']

    log.info('第一名的混淆昵称{0}，分数{1}'.format(first_mixnick, first_gamePoint))
    log.info('提交用户的混淆昵称{0}'.format(context.mixNick))
    ranking = first["ranking"]

    assert ranking == 1, '不是第一名的数据'
    assert first_mixnick == context.mixNick, '第一名混淆昵称相同'


@Given(u'断言昨天{gameDate}的排行榜，前三名，有没有获奖凭证')
def step(context, gameDate):
    url = lancome_url + '/online-game-rankings/list'

    gameType = 'LITTLE_BLACK_BOTTLE'
    request_params = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    res = from_get(request_params, url)
    rank_list = res['responseContent']
    lenght = len(rank_list)
    if lenght == 0:
        assert False, "排行榜数据为空"
    url = lancome_url + '/game-prizes/get-by-mixnick'
    for i in range(lenght):
        item = rank_list[i]
        mixnick = item['mixNick']
        request_parames = {
            'mixNick': mixnick,
            'gameType': gameType
        }
        res = from_get(request_parames, url)

        if i > 3:
            assert res['responseContent']!=None,'第{0}人没有拿到获奖凭证'.format(i)
        else:
            assert res['responseContent'] == None,'第{0}人不应该拿到获奖凭证'.format(i)




