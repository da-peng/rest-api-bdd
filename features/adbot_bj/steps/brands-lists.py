# encoding=utf-8

from behave import *
from utils.base_http import BaseHttp

form_get = BaseHttp().form_get

@Given(u'访问品牌列表{path}')
def step(context, path):
    context.url = context.host + path


@When(u'参数{pageNum}&{pageSize}')
def step(context, pageNum, pageSize):
    url = context.url
    requset_params = {
        'pageNum': int(pageNum),
        'pageSize': int(pageSize),
    }
    response = form_get(requset_params, url)
    context.responseContent = response['responseContent']
