from behave import *
from utils.http_util import HttpUtils
import re
import random
import string

postbytoken = HttpUtils().postBytoken
formget = HttpUtils().form_getBytoken
formpost = HttpUtils().form_postBytoken


@Given(u'查询当前用户{mixNick}已有金币')
def step(context, mixNick):
    url = context.host + '/lppz/gold-coins/get-gold-coins'
    request_params = {
        'mixNick': mixNick
    }
    context.mixNick = mixNick
    res = formget(request_params, url, context.token)
    # goldnum为当前已有金币
    context.goldnum = res['responseContent']


@Given(u'{n}个好友为{userId}点赞,获得金币为{m}枚')
def step(context, n, userId, m):
    path = '/{tenantCode}/thumbs-ups/save/{userId}'
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path_list[3] = userId
    url = context.host + ''.join(path_list)
    #s = string.ascii_lowercase
    s=chr(random.randint(0x4e00, 0x9fbf))
    # 当前后台没有对mixNickFans存不存在做出校验
    mixNickFans = str(s)

    for i in range(1, int(n) + 1):
        request_body = {
            'mixNickFans': mixNickFans + str(i)
        }
        response = postbytoken(request_body, url, context.token)
    context.responseContent = str(context.goldnum + int(2 * int(n)))
    print(context.responseContent)

    assert context.responseContent == str(m), '获得金币数实际为{0}'.format(context.responseContent)


@Then(u'抽奖{l}次，剩余金币为{h}枚')
def step(context, l, h):
    path = '/{tenantCode}/lotterys/go'
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    url = context.host + ''.join(path_list)
    for i in range(int(l)):
        request_body = {
            'mixNick': context.mixNick
        }
        response = formpost(request_body, url, context.token)

    url = context.host + '/lppz/gold-coins/get-gold-coins'
    request_params = {
        'mixNick': context.mixNick
    }
    res = formget(request_params, url, context.token)
    responseContent = res['responseContent']
    assert (int(context.responseContent) / int(8)) >= int(l), '目前金币只能抽{0}次'.format(int(l) - 1)
    assert responseContent == int(h), '剩余金币数实际为{0}'.format(responseContent)
