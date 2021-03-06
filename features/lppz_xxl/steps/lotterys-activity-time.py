from behave import *
from utils.base_http import BaseHttp
import re

form_get = BaseHttp().form_get


@Given(u'访问获取活动时间接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


@When(u'简单FROM_GET请求')
def step(context, ):
    url = context.path
    response = form_get({},url, context.headers)
    context.statusCode = response['statusCode']

