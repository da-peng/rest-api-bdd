# encoding=utf-8

from behave import *
from utils.base_http import BaseHttp

form_get = BaseHttp().form_get


@Given(u'访问品牌渠道账号信息获取接口{path}')
def step(context, path):
    context.url = context.host + path


@When(u'品牌渠道账号信息参数{pageNum}&{pageSize}&{brandCode}&{channelCode}')
def step(context, pageNum, pageSize, brandCode, channelCode):
    url = context.url
    requset_params = {
        'pageNum': int(pageNum),
        'pageSize': int(pageSize),
        'brandCode': brandCode,
        'channelCode': channelCode
    }
    response = form_get(requset_params, url, context.headers)
    context.responseContent = response['responseContent']


