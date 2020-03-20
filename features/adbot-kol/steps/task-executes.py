from behave import *
import re
from utils.base_http import BaseHttp
from service.kol_info import account_id
from utils.file_manage import read

get=BaseHttp().get

@Given(u'访问任务执行详情接口{path}')
def steps(context,path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = context.host + ''.join(path_list)
    request_params={
        'accountId':account_id('adbot_kol_business', read()[3][0])
    }
    response=get(request_params,path,context.headers)
    context.statusCode = response['statusCode']