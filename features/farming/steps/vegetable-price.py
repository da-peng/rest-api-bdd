# encoding=utf-8
from behave import *

from utils.base_http import BaseHttp

post = BaseHttp().post


@given(u"获取蔬菜价格接口{path}")
def step(context, path):
    context.url = context.host + path


@When(u"获取蔬菜价格接口参数{vegetable}&{startTime}&{endTime}")
def step(context, vegetable, startTime, endTime):
    request_body = {
        "vegetable": vegetable,
        "startTime": startTime,
        "endTime": endTime
    }
    response = post(request_body, context.url,{"token":"1111"})
