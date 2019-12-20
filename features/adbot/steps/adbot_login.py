from behave import *
from utils.base_http import BaseHttp
from utils.file_manage import add

post=BaseHttp().post


@Given(u'访问登录接口{path}')
def step(context,path):
    context.url=context.host+path
@When(u'输入账号{username}密码{password}角色{role}')
def step(context,username,password,role):
    response=post(
        {
            "username": username,
            "password": password,
            "componentUUID": "LoginClass_1568105904145"
        },context.url
    )

    context.token=response['responseContent']['token']
    context.role=role
    context.statusCode=response['statusCode']
@Then(u'登陆成功，持久化存储!')
def step(context):
    assert context.statusCode=='20000','登录失败！！！'
    key=context.role
    dict={key:context.token}
    add(dict)