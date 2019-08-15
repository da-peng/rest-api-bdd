from behave import *
from utils.http_util import HttpUtils
from features.lancome.steps.const import lancome_url


from_post = HttpUtils().form_post

@Given(u'访问新增或修改淘宝用户信息接口{path}')
def step(context,path):
    context.url = lancome_url+path


@Then(u'新增或修改淘宝用户信息接口参数{mixNick}&&{nick}')
def step_impl(context,mixNick,nick):

    request_body= {
        'mixNick':mixNick,
        'nick':nick,
    }
    from_post(request_body,context.url)

