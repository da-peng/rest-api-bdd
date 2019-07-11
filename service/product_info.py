#encoding=utf-8
from utils.db_connect import DbConnect
from utils.config_parser import config
from utils.log_manage import Log as log

# 商品管理

def get_product_sku_info(db_name,tenant_code):
    # 商品
    product_info = {}
    connect = DbConnect(db_name)
    # id 就是sku_id
    product_res = connect.query("SELECT product_id,id FROM product_sku WHERE tenant_code = \'" + tenant_code + "\'")

    for product_id, sku_id in product_res:
        if product_id not in product_info.keys():
            product_info[product_id] = []
            product_info[product_id].append(sku_id)
        else:
            product_info[product_id].append(sku_id)
    connect.close()
    return product_info


# NORMAL_PRODUCT,CARD_PRODUCT,SERVE_PRODUCT,LAMPS?
def get_product_info_by_type(db_name,tenant_code, product_type):
    '''
    :param db_name:
    :param tenant_code:
    :param product_type:
    :return: 返回 已经上架线上商城的商品 id和SKU id
    '''

    product_info = {}
    connect = DbConnect(db_name)
    product_res = connect.query("SELECT a.product_id,b.id FROM"
                                "(SELECT DISTINCT product_id FROM  store_product_relationship  WHERE store_type='ONLINE_STORE' AND product_type =\'" + product_type + "\' AND tenant_code = \'" + tenant_code + "\')  AS a LEFT JOIN  product_sku AS b ON a.product_id = b.product_id")

    for product_id, sku_id in product_res:

        if product_id not in product_info.keys():
            product_info[product_id] = []
            product_info[product_id].append(sku_id)
        else:
            product_info[product_id].append(sku_id)
    connect.close()
    log.debug('product_info:' + str(product_info))
    return product_info