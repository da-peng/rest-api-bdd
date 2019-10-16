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

<<<<<<< HEAD
        if i < 3:
            assert res['responseContent']!=None,'第{0}人没有拿到获奖凭证'.format(i)
        else:
            assert res['responseContent'] == None,'第{0}人不应该拿到获奖凭证'.format(i)


@Given(u'{gameDate1}获得过优惠券')
def step(context, gameDate1):
    url = lancome_url + '/online-game-rankings/list'

    gameType = 'LITTLE_BLACK_BOTTLE'
    request_params = {
        'gameDate': gameDate1,
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

        if i < 3:
            assert res['responseContent']!=None,'第{0}人没有拿到获奖凭证'.format(i)
=======
        if i > 3:
            assert res['responseContent']!= None,'第{0}人没有拿到获奖凭证'.format(i)
>>>>>>> 999a142d923ccf2aacf45149a21ab02f83817c73
        else:
            assert res['responseContent'] == None,'第{0}人不应该拿到获奖凭证'.format(i)
    context.firstmixNick=rank_list[0]['mixNick']
@Then(u'{gameDate2},依然是前三名,不会获得优惠券')
def step(context, gameDate2):
    url = lancome_url + '/online-game-rankings/list'

    gameType = 'LITTLE_BLACK_BOTTLE'
    request_params = {
        'gameDate': gameDate2,
        'gameType': gameType
    }
    res = from_get(request_params, url)
    first_gamePoint=res['responseContent'][0]['gamePoint']

    url = lancome_url + '/nascent/point/onlineadd'
    mixNick=context.firstmixNick
    gamePoint = first_gamePoint+1
    gameType = context.gameType
    request_body = {
        'mixNick': mixNick,
        'gameType': gameType,
        'gameUsedSeconds': 10,
        'gamePoint': gamePoint
    }
    from_post(request_body, url)
    url=lancome_url + '/game-prizes/get-by-mixnick'

    request_parames = {
        'mixNick': mixNick,
        'gameType': gameType
    }

    res = from_get(request_parames, url)
    assert res['responseContent'][0] ==0,'此用户获得两次正装奖励'







@Given(u'获取{gameDate}游戏排名')
def step(context,gameDate):
    url = lancome_url + '/online-game-rankings/list'

    gameType = 'LITTLE_BLACK_BOTTLE'
    request_params = {
        'gameDate': gameDate,
        'gameType': gameType
    }
    res = from_get(request_params, url)


@Then(u'{mixNick}提交数据{gamePoint}')
def step(context,mixNick,gamePoint):
    url = lancome_url + '/nascent/point/onlineadd'
    # gamePoint = context.first_gamePoint + 1
    gameType = 'LITTLE_BLACK_BOTTLE'
    request_body = {
        'mixNick': mixNick,
        'gameType': gameType,
        'gameUsedSeconds': 10,
        'gamePoint': gamePoint
    }
    response = from_post(request_body, url)

    context.mixNick = mixNick

