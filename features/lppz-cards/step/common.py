from behave import *
from utils.base_http import BaseHttp

get = BaseHttp().get
post = BaseHttp().post

@When(u'请输入混淆昵称{mixNick}')
def step(context, mixNick):
    url = context.path
    requset_params = {
        'mixNick': mixNick
    }
    response = get(requset_params, url, context.headers)
    context.statusCode = response['statusCode']

# 用于2处接口的feature（address的save和update）

@When(u'输入混淆昵称{mixNick}&用户名{userName}&手机号{mobile}详细地址{detailAddress}地市{city}')
def step(context, mixNick, userName, mobile, detailAddress,city):
    url = context.path
    request_body = {
        'mixNick': mixNick,
        'userName': userName,
        'mobile': mobile,
        'detailAddress': detailAddress,
        'city':city
    }
    response = post(request_body, url, context.headers)
    context.statusCode = response['statusCode']

# 用于所有断言
@Then(u'断言{msg}成功')
def step(context,msg):
    assert context.statusCode == '20000',msg+'失败'
