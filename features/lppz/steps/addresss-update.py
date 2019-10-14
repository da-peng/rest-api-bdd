from behave import *
from utils.http_util import HttpUtils
import re

postbytoken = HttpUtils().postBytoken


@Given(u'访问修改收货地址接口{path}')
def step(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.path = context.host + ''.join(path_list)


# @When(u'输入混淆昵称{mixNick}&用户名{userName}&手机号{mobile}详细地址{fullAddress}')
# def step(context,mixNick,userName,mobile,fullAddress):
#     url = context.path
#     request_body ={
#         'mixNick':mixNick,
#         'userName':userName,
#         'mobile':mobile,
#         'fullAddress':fullAddress
#     }
#     response = postbytoken(request_body, url, token='tlk9juiywan4mrnratkezydgkawmvezl')
#     context.statusCode = response['statusCode']
@Then(u'断言修改收货地址成功')
def step(context):
    assert context.statusCode == '20000', '新增收货地址失败'
