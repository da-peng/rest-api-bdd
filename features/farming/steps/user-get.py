# encoding=utf-8
from behave import *

from utils.base_http import BaseHttp

post = BaseHttp().post


@given(u"获取用户信息接口{path}")
def step(context, path):
    context.url = context.host + path


@When(u"获取用户信息接口参数{uid}")
def step(context, uid):
    request_body = {
        "uid": int(uid)
    }
    response = post(request_body, context.url,{"token":"1111"})
