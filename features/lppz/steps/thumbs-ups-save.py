from behave import *
from utils.http_util import HttpUtils
import re

postbytoken = HttpUtils().postBytoken


@Given(u'访问点赞接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入点赞人混淆昵称{mixNickFans}')
def step(context, mixNickFans):
    url = context.path
    requset_body = {
        'mixNickFans': mixNickFans
    }
    response = postbytoken(requset_body, url, context.token)
    context.statusCode = response['statusCode']


@Then(u'断言点赞成功')
def step(context):
    assert context.statusCode == '20000', '点赞失败'
