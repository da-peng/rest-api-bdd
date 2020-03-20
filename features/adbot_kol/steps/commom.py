from behave import *
from utils.base_http import BaseHttp

get = BaseHttp().get
form_get = BaseHttp().form_get
post = BaseHttp().post

@Then(u'断言{msg}请求成功')
def step(context,msg):
    assert context.statusCode == '20000',msg+'失败'


