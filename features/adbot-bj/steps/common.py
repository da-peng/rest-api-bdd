# encoding=utf-8

from behave import *
from utils.base_http import BaseHttp
import json

get = BaseHttp().get


@Then('断言ResponseContent->list不为空')
def step(context):
    responseContent = context.responseContent
    assert len(responseContent['list']) != 0, '断言失败'
