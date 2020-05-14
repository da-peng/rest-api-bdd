from behave import *
import re
from utils.file_manage import read
from utils.base_http import BaseHttp

get=BaseHttp().get



@Given(u'访问检查wechatSessionKey是否有效接口{path}')
def steps(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.url = context.host + ''.join(path_list)
    request_params={
        'wechatSessionKey':read()[1][1]
    }
    response=get(request_params,context.url,context.headers)
    context.statusCode = response['statusCode']
