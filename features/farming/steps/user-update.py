# encoding=utf-8
from behave import *

from utils.base_http import BaseHttp

post = BaseHttp().post


@given(u"更新用户信息接口{path}")
def step(context, path):
    context.url = context.host + path


@When(u"更新用户信息接口参数{uid}&{nick}&{avatar}")
def step(context, uid, nick, avatar):
    request_body = {
        "uid": uid,
        "nick": nick,
        "avatar": avatar
    }
    response = post(request_body, context.url,{"token":"1111"})
