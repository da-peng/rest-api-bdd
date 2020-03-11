# encoding=utf-8

from behave import *
from utils.base_http import BaseHttp
from features.adbot_bj.utils.data_assembly import assembly_data
import uuid

post = BaseHttp().post


@Then('断言ResponseContent->list不为空')
def step(context):
    responseContent = context.responseContent
    assert len(responseContent['list']) != 0, '断言失败'

@When(u'读取{file_name}数据文件，完成数据组装')
def step(context,file_name):
    request_list = assembly_data(file_name)
    url = context.url
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    # headers = {}
    headers = {'uuid': suid}
    response = post(request_list, url,headers)
    context.statusCode = response['statusCode']

@Then(u'断言statusCode===200')
def step(context):
    pass