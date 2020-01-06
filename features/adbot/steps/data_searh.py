from behave import *
from utils.base_http import BaseHttp
import re

form_get=BaseHttp().form_get
@Given(u'访问数据检索接口{path}')
def step(context,path):
    path_list=re.split('{|}',path)
    path_list[1]=context.tenant_code
    context.path=context.host+''.join(path_list)

@When(u'输入参数{domain}&{username}')
def step(context,domain,username):
    url=context.path
    requset_params={
        'domain':domain,
        'username':username,
        'pageNum':'1',
        'pageSize':'15'
    }
    response=form_get(requset_params,url,context.headers)
    context.statusCode=response['statusCode']
@Then(u'搜索成功')
def step(context):
    assert context.statusCode=='20000','搜索失败'





