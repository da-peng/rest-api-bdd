# encoding=utf-8
from behave import *

from utils.base_http import BaseHttp

get = BaseHttp().get


@given(u"获取蔬菜列表接口{path}")
def step(context, path):
    context.url = context.host + path
    response = get({}, context.url, {"token": "1111"})
