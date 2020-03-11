from behave import *
from utils.base_http import BaseHttp
import re

post = BaseHttp().post


@Given(u'访问邀请好友接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'请输入淘宝用户id{userId}&受邀人的混淆昵称{mixNickFans}')
def step(context,userId,mixNickFans):
    url = context.path
    requset_params = {
        'userId': userId,
        'mixNickFans':mixNickFans,
    }
    response = post(requset_params, url, context.headers)
    context.statusCode = response['statusCode']