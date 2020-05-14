# encoding=utf-8
import hashlib

from behave import *

from utils.base_http import BaseHttp

post = BaseHttp().post


@given(u"爬虫蔬菜价格接口{path}")
def step(context, path):
    context.url = context.host + path


@When(u"爬虫蔬菜价格接口参数{startTime}&{endTime}")
def step(context, startTime, endTime):
    request_body = {
        "startTime": startTime,
        "endTime": endTime
    }
    response = post(request_body, context.url,{'token':'111'})
