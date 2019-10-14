from behave import *
from utils.http_util import HttpUtils
import re

formget = HttpUtils().form_getBytoken


@Given(u'访问点赞好友列表接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'输入混淆昵称{mixNick}&页码{pageNum}&每页大小{pageSize}')
def step(context, mixNick, pageNum, pageSize):
    url = context.path
    requset_params = {
        'mixNick': mixNick,
        'pageNum': pageNum,
        'pageSize': pageSize
    }
    response = formget(requset_params, url, context.token)
    context.statusCode = response['statusCode']


@Then(u'断言点赞好友列表接口访问成功')
def step(context):
    assert context.statusCode == '20000', '接口访问失败'
