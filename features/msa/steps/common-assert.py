# encoding=utf-8
from behave import *


@Then(u'断言statusCode===20000')
def step_impl(context):
    response = context.response
    statusCode= response['statusCode']
    assert statusCode == '20000'
