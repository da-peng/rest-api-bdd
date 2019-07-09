# encoding=utf-8
from behave import *

from utils.http_util import HttpUtils
from utils.file_manage import  add



post = HttpUtils().post
@Given("访问登录接口 {path}")
def step_impl(context, path):
    context.url = context.host + path


@Given("{role}账号{account}和{password}")
def step_impl(context,role, account, password):

    response = post({
        "username": account,
        "password": password
    }, context.url
    )
    context.role = role
    context.token = response['responseContent']['token']

@Then('持久化存储token')
def step_impl(context):
    key = context.role
    add({key:context.token})