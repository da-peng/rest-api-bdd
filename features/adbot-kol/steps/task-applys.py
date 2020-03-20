from behave import *
import re
from utils.base_http import BaseHttp
from service.kol_info import account_id
from utils.file_manage import read

post = BaseHttp().post


@Given(u'访问kol报名任务接口{path}')
def steps(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = context.host + ''.join(path_list)
    context.url = path


@When(u'输入参数{taskStoreId},{taskProjectId}')
def steps(context, taskStoreId, taskProjectId):
    requesu_body = {
        'accountId': account_id('adbot_kol_business', read()[3][0]),
        'taskStoreId': taskStoreId,
        'taskProjectId': taskProjectId

    }
    response = post(requesu_body, context.url, context.headers)
    context.statusCode = response['statusCode']