# encoding=utf-8

from behave import *

from features.utils.http_util import  *

lancome_url = "http://lancome.meizhidev.com/lancome"


@Given("访问接口 {path}")
def step_impl(context, path):
    context.url = lancome_url + path
    print('* '*5+'URL'+' *'*5)
    print(context.url)


@given('请求参数：混淆昵称及积分')
def step_impl(context):
    for row in context.table:
        taobaoId = row['taobaoId']
        point = row['point']

        request_body = {
            "taobaoId": taobaoId,
            "pointSource": "GAME",
            "point": point,
            "expiredTime": "2019-10-12"
        }
        HttpUtils().post(request_body,context.url)



