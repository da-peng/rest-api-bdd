from behave import *
from utils.http_util import HttpUtils

getbytoken = HttpUtils().form_getBytoken
postbytoken = HttpUtils().postBytoken


@When(u'请输入混淆昵称{mixNick}')
def step(context, mixNick):
    url = context.path
    requset_params = {
        'mixNick': mixNick
    }
    response = getbytoken(requset_params, url, context.token)
    context.statusCode = response['statusCode']


@When(u'输入混淆昵称{mixNick}&用户名{userName}&手机号{mobile}详细地址{fullAddress}')
def step(context, mixNick, userName, mobile, fullAddress):
    url = context.path
    request_body = {
        'mixNick': mixNick,
        'userName': userName,
        'mobile': mobile,
        'fullAddress': fullAddress
    }
    response = postbytoken(request_body, url, context.token)
    context.statusCode = response['statusCode']
