# encoding=utf-8
from behave import *
from service.activity_group import *
from utils.time_manage import *
from utils.log_manage import Log as log
from utils.base_http import BaseHttp
import re

postByToken = BaseHttp().postByToken

Parameter = {
    'uat': {
        'storeId': 206,
        'storeCode': '20190604162222079186726074610008',
        'payAppCode': 'AMILY-pay-02'
    },
    'test': {
        'storeId': 78,
        'storeCode': '2018053411171988358387898510001',
        'payAppCode': 'linqingxuan-pay-02'
    }

}


@Given(u'访问开团接口 {path}')
def step_impl(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = ''.join(path_list)

    db_marketing = 'msa_marketing'
    db_order = 'msa_order'
    context.url = context.host + path
    context.db_order = context.db_prefix + db_order
    context.db_marketing = context.db_prefix + db_marketing


@Given(u'开团用户及活动信息{wechatAccountId}&{purchases}&{addressId}')
def step_impl(context, wechatAccountId, purchases, addressId):
    '''
    开团操作
    :param context:
    :param wechatAccountId:
    :param purchases:
    :param addressId:
    :return:
    '''
    env = context.env
    Parame = Parameter[env]
    storeId = Parame['storeId']
    storeCode = Parame['storeCode']
    payAppCode = Parame['payAppCode']

    tenant_code = context.tenant_code
    db_marketing = context.db_marketing

    activity_info = get_activity_by_type(db_marketing, tenant_code, 'GROUP')
    log.info('activity_info:{0}'.format(activity_info))

    payment_order_id_and_code = {}

    for i in activity_info.keys():
        activity_group_id = i
        product_info = activity_info[i]
        product_id_list = list(product_info.keys())
        product_id = product_id_list[0]  # 取活动的商品列表的第一个商品
        product_sku_id = product_info[product_id][0]  # 取商品的sku列表的第一个SKU

        response = postByToken(
            {
                "wechatAccountId": wechatAccountId,
                "activityGroupId": activity_group_id,
                "productId": product_id,
                "productSkuId": str(product_sku_id),
                "purchases": "1",
                "formId": "the formId is a mock one",
                "storeId": storeId,  # 商店id，可固定
                "storeCode": storeCode,  # 可固定
                "payAppCode": payAppCode,
                "addressId": addressId
            }, context.url
            , 'consumer'
        )

        try:
            response_content = response['responseContent']
            order_id = response_content['orderId']
            payment_order_code = response_content['orderMap']['paymentOrderCode']
            if order_id not in payment_order_id_and_code:
                payment_order_id_and_code[order_id] = payment_order_code
            log.info('活动ID:{0}开团成功'.format(activity_group_id))
        except Exception as e:
            # {"statusCode": "20400", "statusMessage": "您还有未完成的拼团订单,请先处理吧~"}
            log.info(str(response))
            log.info('活动ID:{0}已经开团了;可忽略这个错误'.format(activity_group_id))
        sleep()
    context.response = response

    context.payment_order_id_and_code = payment_order_id_and_code


@Then(u'拿到paymentOrderCode和orderid')
def step_impl(context):
    '''
    删除数据
    :param context:
    :return:
    '''
    payment_order_id_and_code = context.payment_order_id_and_code
    for i in payment_order_id_and_code.keys():
        log.debug('orderId:{0},payment_order_id_and_code:{1}'.format(i, str(payment_order_id_and_code[i])))
        # update_order_status(context.db_order,i)
        # 这里不能光更新订单状态，涉及到活动，还有活动状态


@Given(u'访问订单状态接口 {path} 并构建参数请求{userId}')
def step_impl(context, path, userId):
    '''
    只支持普通订单
    :param context:
    :param path:
    :param userId:
    :return:
    '''
    path_list = re.split('{|}', path)

    payment_order_id_and_code = context.payment_order_id_and_code
    for i in payment_order_id_and_code.keys():
        order_id = i

        path_list[1] = context.tenant_code
        path_list[3] = str(order_id)

        path = ''.join(path_list)
        url = context.host + path
        response = postByToken(
            {
                "userId": str(userId),
                "paymentCode": payment_order_id_and_code[i],
                "payTime": getCurrentTime()
            }, url,
            'manager'
        )
        sleep()
    log.info('完成所有支付订单状态更新')


if __name__ == '__main__':
    str1 = '/baiyang/sale-orders/{orderId}/update-payment-status'
    list1 = re.split('{|}', str1)
    list1[1] = '111'
    path = ''.join(list1)
    print(path)

    print((datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"))
