from behave import *
from utils.base_http import BaseHttp
from utils.file_manage import *

post=BaseHttp().post


@Given(u'访问登录接口{path}')
def step(context,path):
    context.url=context.host+path
@When(u'输入账号{username}密码{password}')
def step(context,username,password):
    response=post(
        {
            "username": username,
            "password": password,
            "componentUUID": "LoginClass_1568105904145"
        },context.url
    )

    context.token=response['responseContent']['token']
    context.statusCode=response['statusCode']
@Then(u'登陆成功，持久化存储!')
def step(context):
    assert context.statusCode=='20000','登录失败！！！'
    write(context.token)
