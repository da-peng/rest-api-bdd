#encoding=utf-8
from utils.db_connect import DbConnect
from utils.config_parser import config
# GROUP
# 活动管理
def get_activity_by_type(db_name,tenant_code, activity_type):
    activity_info = {}
    connect = DbConnect(db_name)
    activity_res = connect.query("SELECT DISTINCT b.activity_id,c.product_id,c.sku_id "
                                 "FROM "
                                 "(SELECT activity_id,product_id,status FROM(SELECT id,activity_name FROM activity_group WHERE activity_start_time<= now() AND activity_end_time > now()) "
                                 "AS a LEFT JOIN activity_product ON a.id = activity_id) "
                                 "AS b LEFT JOIN activity_product_sku AS c ON b.product_id = c.product_id "
                                 "AND  tenant_code =  \'" + tenant_code + "\' AND activity_type =\'" + activity_type + "\' AND b.status ='ENABLE'")

    for activity_id, product_id, sku_id in activity_res:
        # log.info('{0},{1},{2}'.format(activity_id,product_id,sku_id))
        if activity_id not in activity_info.keys():
            activity_info[activity_id] = {}
            activity_info[activity_id][product_id] = []
            activity_info[activity_id][product_id].append(sku_id)
        else:
            if product_id not in  activity_info[activity_id].keys():
                activity_info[activity_id][product_id] = []
                activity_info[activity_id][product_id].append(sku_id)
            else:
                activity_info[activity_id][product_id].append(sku_id)

    connect.close()

    return activity_info

# 商品管理

def get_product_sku_info(db_name,tenant_code):
    # 商品
    # db_name = 'uat_msa_store'
    product_info = {}
    connect = DbConnect(db_name)
    # id 就是sku_id
    product_res = connect.query("SELECT product_id,id FROM product_sku WHERE tenant_code = \'" + tenant_code + "\'")
    env = config['env']['TEST_ENV']
    for product_id, sku_id in product_res:
        if env == 'test':
            if product_id > 1000:
                continue
            else:
                break
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
    return product_info

if __name__ == '__main__':
    # 更新所有已经过期的活动，的状态
    db_name = 'msa_marketing'
    tenant_code = 'lqx'
    product_info = {}
    connect = DbConnect(db_name)
    connect.update(" UPDATE `activity_group` SET `status` = 'DELETE' "
                   "WHERE activity_end_time < now() and tenant_code = \'"+tenant_code+"\'")



