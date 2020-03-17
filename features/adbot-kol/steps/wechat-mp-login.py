from behave import *
from utils.base_http import BaseHttp


form_post=BaseHttp().form_post


@Given(u'访问微信小程序登录接口{path}，输入参数{code},{inviteCode}')
def steps(context,path,code,inviteCode):
    context.path=context.host+str(path)
    requset_body={
        'code':code,
        'inviteCode':inviteCode
    }
    response=form_post(requset_body,context.path)
    context.statusCode=response['statusCode']




