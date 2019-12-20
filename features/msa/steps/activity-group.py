# encoding=utf-8
from behave import *
from utils.time_manage import *
from service.product_info import *
from utils.base_http import BaseHttp
from utils.log_manage import Log as log
from random import *
import re

postByToken = BaseHttp().postByToken


@Given(u"访问创建拼团活动接口 {path}")
def step_impl(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = ''.join(path_list)

    db_store = 'msa_store'
    context.url = context.host + path
    context.db_store = context.db_prefix + db_store


@Given(u"创建{nums}个活动；活动信息{product_type}&{groupDurationHours}&{groupCompletePeoples}&{activityProductLimit}")
def step_impl(context, nums, product_type, groupDurationHours, groupCompletePeoples, activityProductLimit):
    tenant_code = context.tenant_code
    db_store = context.db_store

    activity_name_list = []
    product_info = get_product_info_by_type(db_store, tenant_code, product_type)
    log.debug('{0}'.format(product_info))
    product_list = list(product_info.keys())
    length = len(product_list)
    if length < int(nums):
        nums = length

    for i in range(int(nums)):
        current_time = str(getCurrentTime())
        activity_name = "拼__团_{0}人团{1}".format(randint(2, int(groupCompletePeoples)), get_time_stamp())
        end_time = str(getEndTime())

        product_id = choice(product_list)
        # sku_id = product_info[product_id][0]  # 取第一个 一个商品ID会有多个SKU 都取第一个

        skuParamList = []
        for i in product_info[product_id]:
            skuParam = {
                "skuId": i,
                "activityPrice": randint(0, 100) / 10
            }
            skuParamList.append(skuParam)

            # product_id, sku_id = product_info[i]

        response = postByToken({
            "addActivityProductList": [{
                "productId": product_id,
                "skuParamList": skuParamList
            }],
            "activityName": activity_name,
            "activityStartTime": current_time,
            "activityEndTime": end_time,
            # "activityBanner": "https://aliyun-oss-msa.meizhidev.com/templates/20190605/db3c7053ee8d3d941481e84b5d1f1401/0",
            "activityBanner": "https://aliyun-oss-msa.meizhidev.com/templates/20190627/1849fb13493b1fafc8f863ba64d92763/0",
            "groupDurationHours": groupDurationHours,
            "groupCompletePeoples": groupCompletePeoples,
            "activityProductLimit": activityProductLimit,
            "showFlag": "YES",
            "remark": "活动规则",
            "activityStatus": "AVAILABLE"
        }, context.url
            , 'manager')

        activity_name_list.append(activity_name)
        sleep()  # sleep 5秒
    # context.groupActivityName = activity_name_list
    context.response = response

    log.info('创建活动{0}个;活动名称:{1}'.format(len(activity_name_list) + 1, ','.join(activity_name_list)))

# @Then(u'持久化存储活动名称')
# def step_impl(context):
#     group_activity_name = context.groupActivityName
#     log.info('创建活动{0}个;活动名称:{1}'.format(len(group_activity_name) + 1, ','.join(group_activity_name)))
#     add({'group_activity_name': context.groupActivityName})


# if __name__ == '__main__':
# str1 = '/baiyang/sale-orders/{orderId}/update-payment-status'
# list1 = re.split('{|}',str1)
# # print(time.time())
# print(list1)
# print(get_time_stamp())
# print(get_product_info_by_type(db_name, tenant_code, 'NORMAL_PRODUCT'))

# print((datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"))
