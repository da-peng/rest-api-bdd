# encoding=utf-8
import time
import uuid
import re
import asyncio
import os
from behave import *
from utils.base_http import BaseHttp
from features.adbot_bj.utils.data_assembly import assembly_data
from utils.log_manage import Log as logs

post = BaseHttp().post


@Given(u'{api_name}接口{path}')
def step(context, api_name, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    context.url = context.host + ''.join(path_list)
    logs.debug("接口名称:%s" % api_name)


@Then('断言ResponseContent->list不为空')
def step(context):
    responseContent = context.responseContent
    assert len(responseContent['list']) != 0, '断言失败'


def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        endtime = time.time() - start
        # logs.debug(":" + api_name)
        return ret

    return wrapper


@log
@When(u'读取{file_name}数据文件，完成数据组装')
def step(context, file_name):
    size = 2
    request_list = assembly_data(file_name, size)
    if not request_list:
        raise Exception('测试数据组装异常')
    url = context.url
    # 时间循环加协程， await 异步刮起，此时不等待开启另一个task；提升效率
    loop = asyncio.get_event_loop()
    task = [asyncio.ensure_future(async_post(i, request_list, url)) for i in range(len(request_list))]
    start = time.time()
    loop.run_until_complete(asyncio.wait(task))
    end_time = time.time() - start
    loop.close()
    logs.debug('耗时:%.2f s' % end_time)
    print()
    project_path = os.path.abspath(os.path.dirname(__file__)).split('adbot_bj')[0]
    with open(os.path.join(project_path, 'adbot_bj/report/concurrence'), 'a') as fp:
        fp.writelines('接口:%s,耗时:%.2f s\n' % (file_name, end_time))


async def async_post(i, request_list, url):
    uid = str(uuid.uuid4())
    # suid = ''.join(uid.split('-'))
    # headers = {}
    headers = {'uuid': uid}
    response = await post(request_list[i], url, headers)
    statusCode = response['statusCode']
    assert statusCode == "20000", "请求异常"


@Then(u'断言statusCode===20000')
def step(context):
    pass
    # assert context.statusCode == "20000", "请求异常"
