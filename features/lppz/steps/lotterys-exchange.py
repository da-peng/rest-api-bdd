from behave import *
from utils.http_util import HttpUtils
import re

formpost = HttpUtils().form_postBytoken


@Given(u'访问领取优惠券接口{path}，输入混淆昵称{mixNick}&奖品id{prizeId}&奖品类型{type}')
def step(context, path, mixNick, prizeId,type):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)
    request_body = {
        'mixNick': mixNick,
        'prizeId': prizeId,
        'type':type
    }
    response = formpost(request_body, context.path, context.token)
    context.statusCode = response['statusCode']


@Then(u'断言领取优惠券成功')
def step(context):
    assert context.statusCode == '20000', '领取优惠券失败'
