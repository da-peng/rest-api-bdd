# encoding=utf-8
from behave import *

from utils.base_http import BaseHttp

post = BaseHttp().post


@given(u"注册接口{path}")
def step(context, path):
    context.url = context.host + path


@When(u"参数{username}&{password}")
def step(context, username, password):
    request_body = {
        "username": username,
        "password": password
    }
    response = post(request_body, context.url)
