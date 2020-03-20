from behave import *
import re
from utils.base_http import BaseHttp
from service.kol_info import *

post = BaseHttp().post


@Given(u'访问kol账号审核接口{path},输入参数{kolId},{approvalRemark},{approvalStatus}')
def steps(context, path, kolId,approvalRemark, approvalStatus):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code

    path_list[3] = str(id('adbot_kol_business', ))
    url = context.host + ''.join(path_list)
    request_body = {
        "id": id( ),
        "kolId": kolId,
        "approvalRemark": approvalRemark,
        "approvalStatus": approvalStatus
    }
    response = post(request_body, url, context.headers)
    context.statusCode = response['statusCode']



if __name__=='__main__':
    path='/kol/{tenantCode}/kol-accounts/approval-status/{id}'
    a=re.split('{|}',path)
    print(a)