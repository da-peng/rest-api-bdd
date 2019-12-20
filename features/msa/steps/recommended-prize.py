# encoding=utf-8
from behave import *
from utils.time_manage import *
from service.coupon_info import *
from service.product_info import *
from utils.base_http import BaseHttp
from random import *
import re

postByToken = BaseHttp().postByToken

@Given(u"访问推荐有奖创建接口 {path}")
def step_impl(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = ''.join(path_list)

    db_store = 'msa_store'
    db_marketing = 'msa_marketing'
    context.url = context.host + path
    context.db_marketing = context.db_prefix + db_marketing
    context.db_store = context.db_prefix + db_store


@Given(u"创建{nums}个推荐有奖活动，活动信息{product_num}&{product_type}")
def step_impl(context, nums, product_num, product_type):
    tenant_code = context.tenant_code
    db_marketing = context.db_marketing
    db_store =  context.db_store

    coupon_ids = get_coupon_info(db_marketing, tenant_code)
    product_info = get_product_info_by_type(db_store, tenant_code, product_type)

    product_list = list(product_info.keys())
    length = len(product_list)
    if length < int(nums):
        nums = length

    for i in range(int(nums)):

        current_time = str(getCurrentTime())
        activity_name = "推荐有奖_{0}".format(get_time_stamp())
        end_time = str(getEndTime())

        product_id = choice(product_list)
        # sku_id = product_info[product_id][0]  # 取第一个 一个商品ID会有多个SKU 都取第一个

        skuParamList = []
        for i in product_info[product_id]:
            skuParam = {
                "skuId": i,
                "couponId": choice(coupon_ids)[0],
                "discountPercent": randint(10, 100),
                "usableFlag": "YES"
            }
            skuParamList.append(skuParam)

        response = postByToken(
            {
                "activityStartTime": current_time,
                "activityEndTime": end_time,
                "activityName": activity_name,
                "activityRemark": "推荐有奖",
                "activityStatus": "AVAILABLE",
                "addActivityProductList": [{
                    "productId": product_id,
                    "skuParamList": skuParamList
                }],
            }
            , context.url
            , 'consumer'
        )
    context.response = response
