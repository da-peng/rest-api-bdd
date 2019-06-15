# # encoding=utf-8
#
# from behave import *
#
# lancome_url = "http://lancome-test.meizhidev.com/lancome"
#
#
# @Given("访问接口 {path}")
# def step_impl(context, path):
#     context.url = lancome_url + path
#     print('* '*5+'URL'+' *'*5)
#     print(context.url)
#
#
# @given('请求参数：混淆nick/耗时')
# def step_impl(context):
#     for row in context.table:
#         mixNick = row['mixNick']
#         gameUsedSeconds = row['gameUsedSeconds']
#         # mixNick = mixNick.encode("GB2312")
#         request_body = {
#             "mixNick": mixNick,
#             "gameType": "ROSE_LABORATORY",
#             "gameUsedSeconds": int(gameUsedSeconds)
#         }
#         HttpUtils().form_post(request_body,context.url)
#         # HttpUtils().post(request_body,context.url)
#
#
