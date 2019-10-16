from behave import *
from utils.http_util import HttpUtils
import re

postbytoken = HttpUtils().form_postBytoken


@Given(u'访问赚金币接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入赚金币类型{sourceType}&收藏加购商品{productCode}&混淆昵称{mixNick}')
def step(context, sourceType, productCode, mixNick):
    url = context.path

    request_body = {
        'sourceType': sourceType,
        'productCode': productCode,
        'mixNick': mixNick
    }
    response = postbytoken(request_body, url, context.token)
    context.statusCode = response['statusCode']


@Then(u'断言赚取金币成功')
def step(context):
    assert context.statusCode == '20000', '赚取金币失败'
