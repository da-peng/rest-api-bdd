# encoding=utf-8
from behave import *


@Then(u'断言statusCode===20000')
def step_impl(context):
    response = context.response
    statusCode= response['statusCode']
    print(statusCode)
    assert statusCode == '20000'


@Then(u'断言status===200')
def step_impl(context):
    response = context.response
    status= response['status']
    assert status == '200'

