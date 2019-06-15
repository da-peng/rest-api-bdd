#encoding=utf-8
from utils.db_connect import DbConnect

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
    product_info = {}
    connect = DbConnect(db_name)
    product_res = connect.query("SELECT product_id,b.id FROM"
                                "(SELECT id FROM product WHERE product_type =\'" + product_type + "\' and tenant_code = \'" + tenant_code + "\')  AS a LEFT JOIN  product_sku AS b ON a.id = b.product_id")
    for product_id, sku_id in product_res:
        if product_id not in product_info.keys():
            product_info[product_id] = []
            product_info[product_id].append(sku_id)
        else:
            product_info[product_id].append(sku_id)
    connect.close()
    return product_info

