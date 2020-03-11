# encoding=utf-8

from behave import *
from utils.base_http import BaseHttp
from features.adbot_bj.utils.data_assembly import assembly_data
import uuid
import re
from utils.log_manage import Log as log

post = BaseHttp().post

@Given(u'{api_name}接口{path}')
def step(context,api_name,path):
    path_list=re.split('{|}',path)
    path_list[1]=context.tenant_code
    context.url=context.host+''.join(path_list)
    log.debug("接口名称:"+api_name)

@Then('断言ResponseContent->list不为空')
def step(context):
    responseContent = context.responseContent
    assert len(responseContent['list']) != 0, '断言失败'

@When(u'读取{file_name}数据文件，完成数据组装')
def step(context, file_name):
    request_list = assembly_data(file_name)
    if request_list==[]:
       raise Exception('请求测试数据组装异常')
    url = context.url
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    # headers = {}
    headers = {'uuid': suid}
    response = post(request_list, url, headers)
    context.statusCode = response['statusCode']


@Then(u'断言statusCode===20000')
def step(context):
    assert context.statusCode == "20000","请求异常"
