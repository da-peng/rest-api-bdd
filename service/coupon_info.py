#encoding=utf-8
from utils.db_connect import DbConnect
from utils.config_parser import config
from utils.log_manage import Log as log


def get_coupon_info(db_name,tenant_code):
    connect = DbConnect(db_name)
    sql = "SELECT id FROM coupon WHERE stock> 50 AND tenant_code =  \'" + tenant_code + "\' AND STATUS='ENABLE' " \
        "AND coupon_type='COUPON' AND discount_type='VOUCHER' AND coupon_status='PUBLISHED' " \
         "AND approve_status='APPROVE_PASS'"
    coupon_ids = connect.query(sql)

    connect.close()
    log.debug('coupon_ids:'+str(coupon_ids))
    return coupon_ids