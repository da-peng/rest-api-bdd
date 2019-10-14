from behave import *
from utils.http_util import HttpUtils
import re

formget = HttpUtils().form_getBytoken


@Given(u'访问用户点赞数、当日新增、排名接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


# @When(u'输入混淆昵称{mixNick}')
# def step(context, mixNick):
#     url = context.path
#     requset_params = {
#         'mixNick': mixNick
#     }
#     response = formget(requset_params, url, token='tlk9juiywan4mrnratkezydgkawmvezl')
#     context.statusCode = response['statusCode']

@Then(u'断言用户点赞数、当日新增、排名接口访问成功')
def step(context):
    assert context.statusCode == '20000', '用户点赞数、当日新增、排名接口访问失败'
