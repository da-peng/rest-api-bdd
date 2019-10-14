from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url


from_get = HttpUtils().form_get

@Given(u'访问是否提供过会员名接口{path}')
def step(context,path):
    context.url = lancome_url+path


@Then(u'是否提供过会员名接口参数{mixNick}')
def step_impl(context,mixNick):

    request_params= {
        'mixNick':mixNick,
    }
    from_get(request_params,context.url)

