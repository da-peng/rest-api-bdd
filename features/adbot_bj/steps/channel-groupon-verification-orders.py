#encoding=utf-8
from behave import  *
import re

@Given(u'团购核销单新增或者更新{path}')
def step(context,path):
    path_list=re.split('{|}',path)
    path_list[1]=context.tenant_code
    context.url=context.host+''.join(path_list)