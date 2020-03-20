from behave import *
from utils.base_http import BaseHttp
from utils.csv_manage import CSVManager

form_post = BaseHttp().post
fp = CSVManager('features/adbot_kol/test-data/login.csv')


@Given(u'访问微信小程序登录接口{path}，输入参数{code},{inviteCode}')
def steps(context, path, code, inviteCode):
    context.path = context.host + str(path)
    requset_body = {
        'code': code,
        'inviteCode': inviteCode
    }
    response = form_post(requset_body, context.path)
    context.statusCode = response['statusCode']
    context.wechatSessionKey = response['responseContent']['wechatSessionKey']
    context.wechatAccountId = response['responseContent']['wechatAccountId']
    context.token = response['responseContent']['token']


@Then(u'储存微信信息')
def steps(context):
    fp.write(['token', 'wechatSessionKey', 'wechatAccountId'],
            [context.token, context.wechatSessionKey, context.wechatAccountId])
