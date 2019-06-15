# encoding=utf-8
from behave import *
from utils.time_mange import *
from service.activity_group import *
from utils.http_util import HttpUtils
from utils.file_manage import add
from utils.log_manage import Log as log

postByToken = HttpUtils().postByToken
post = HttpUtils().post


tenant_code = 'baiyang'
db_name = 'uat_msa_store'


@Given("访问创建拼团活动接口 {path}")
def step_impl(context, path):
    context.url = context.host + path


@Given("创建{nums}个活动；活动信息{product_type}&{groupDurationHours}&{groupCompletePeoples}&{activityProductLimit}")
def step_impl(context, nums, product_type, groupDurationHours, groupCompletePeoples, activityProductLimit):
    activity_name_list = []
    product_info = get_product_info_by_type(db_name, tenant_code, product_type)
    log.debug('{0}'.format(product_info))
    product_list = list(product_info.keys())
    length = len(product_list)
    if length < int(nums):
        nums = length

    for i in range(int(nums)):
        current_time = str(getCurrentTime())
        activity_name = "拼团_" + get_time_stamp()
        end_time = str(getEndTime())

        product_id = product_list[i]
        sku_id = product_info[product_id][0]  # 取第一个 一个商品ID会有多个SKU 都取第一个
        # product_id, sku_id = product_info[i]

        response = postByToken({
            "addActivityProductList": [{
                "product_id": product_id,
                "skuParamList": [{
                    "sku_id": sku_id,
                    "activityPrice": 0.01
                }]
            }],
            "activity_name": activity_name,
            "activityStartTime": current_time,
            "activityEndTime": end_time,
            # "activityBanner": "https://aliyun-oss-msa.meizhidev.com/templates/20190605/db3c7053ee8d3d941481e84b5d1f1401/0",
            "activityBanner": "https://aliyun-oss-msa.meizhidev.com/templates/20190606/52aa82bf7ee19fbb44304b0195b9ecf4/0",
            "groupDurationHours": groupDurationHours,
            "groupCompletePeoples": groupCompletePeoples,
            "activityProductLimit": activityProductLimit,
            "showFlag": "YES",
            "remark": "活动规则",
            "activityStatus": "AVAILABLE"
        }, context.url
        )
        activity_name_list.append(activity_name)
        sleep()  # sleep 5秒
    context.groupActivityName = activity_name_list


@Then('持久化存储活动名称')
def step_impl(context):
    group_activity_name = context.groupActivityName
    log.info('创建活动{0}个;活动名称:{1}'.format(len(group_activity_name) + 1, ','.join(group_activity_name)))
    add({'group_activity_name': context.groupActivityName})


if __name__ == '__main__':
    # str1 = '/baiyang/sale-orders/{orderId}/update-payment-status'
    # list1 = re.split('{|}',str1)
    # # print(time.time())
    # print(list1)
    # print(get_time_stamp())
    print(get_product_info_by_type(db_name, tenant_code, 'NORMAL_PRODUCT'))

    # print((datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"))
