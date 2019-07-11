#encoding=utf-8
from utils.db_connect import DbConnect
from utils.config_parser import config
from utils.log_manage import Log as log
# GROUP

def update_order_status(db_name,order_id):
    connect = DbConnect(db_name)
    sql = "UPDATE sale_order SET order_status = 'ORDER_PAYMENT_SUCCESS' WHERE id = "+str(order_id)+""
    connect.update(sql)
    log.debug('update_order_status:'+sql)
    connect.close()

# 活动管理
def get_activity_by_type(db_name,tenant_code, activity_type):
    activity_info = {}
    connect = DbConnect(db_name)
    activity_res = connect.query("SELECT DISTINCT b.activity_id,c.product_id,c.sku_id "
                                 "FROM "
                                 "(SELECT DISTINCT activity_id,product_id,status FROM(SELECT id,activity_name FROM activity_group WHERE activity_start_time<= now()"
                                 " AND activity_end_time > now() AND activity_status = 'AVAILABLE' AND  tenant_code =  \'" + tenant_code + "\')"
                                 "AS a LEFT JOIN activity_product ON a.id = activity_id) "
                                 "AS b LEFT JOIN activity_product_sku AS c ON b.product_id = c.product_id "
                                 " AND activity_type =\'" + activity_type + "\' AND b.status ='ENABLE'")

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



if __name__ == '__main__':
    # 更新所有已经过期的活动，的状态
    db_name = 'msa_marketing'
    tenant_code = 'lqx'
    product_info = {}
    connect = DbConnect(db_name)
    connect.update(" UPDATE `activity_group` SET `status` = 'DELETE' "
                   "WHERE activity_end_time < now() and tenant_code = \'"+tenant_code+"\'")



