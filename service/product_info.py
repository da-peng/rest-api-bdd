#encoding=utf-8
from utils.db_connect import DbConnect
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
                                "(SELECT DISTINCT product_id FROM  store_product_relationship  WHERE store_type= 'ONLINE_STORE' AND product_type =\'" + product_type + "\' AND tenant_code = \'" + tenant_code + "\')  AS a LEFT JOIN  product_sku AS b ON a.product_id = b.product_id")

    for product_id, sku_id in product_res:


        if product_id not in product_info.keys():
            product_info[product_id] = []
            product_info[product_id].append(sku_id)
        else:
            product_info[product_id].append(sku_id)
    connect.close()
    log.debug('product_info:' + str(product_info))
    return product_info
def get_prodict_classify_info(db_name):
    classify_info={}
    spename_info={}
    spevalue_info={}
    classify_specname={}
    specname_specvalue={}
    connect=DbConnect(db_name)
    product_res=connect.query("SELECT a.spec_name,a.specification_id,a.spec_value,a.value_id,a.product_classify_id,product_classify.classify_name FROM (SELECT product_specification.spec_name,product_specification.id AS specification_id,product_specification_value.spec_value,product_specification_value.id AS value_id,product_specification.product_classify_id FROM product_specification LEFT JOIN product_specification_value ON product_specification.product_classify_id=product_specification_value.product_classify_id AND product_specification.id=product_specification_value.spec_id WHERE product_specification.status='ENABLE' AND product_specification_value.status='ENABLE' AND product_specification.tenant_code='lqx') AS a LEFT JOIN product_classify ON a.product_classify_id=product_classify.id WHERE product_classify.classify_type='PRODUCT' AND product_classify.tenant_code='lqx'")
    for spec_name,specification_id,spec_value,value_id,product_classify_id,classify_name in product_res:
        if classify_name not in classify_info.keys():
            classify_info[classify_name]=product_classify_id
        if spec_name not in spename_info.keys():
            spename_info[spec_name]=specification_id
        if spec_value not in spevalue_info.keys():
            spevalue_info[spec_value]=value_id
    for spec_name, specification_id, spec_value, value_id, product_classify_id, classify_name in product_res:
        if classify_name not in classify_specname.keys():
            classify_specname[classify_name]=[]
            classify_specname[classify_name].append(spec_name)
        else:
            classify_specname[classify_name].append(spec_name)
        #字典value列表去重
        classify_specname[classify_name]=list(set(classify_specname[classify_name]))

    for spec_name, specification_id, spec_value, value_id, product_classify_id, classify_name in product_res:
        if spec_name not in specname_specvalue.keys():
            specname_specvalue[spec_name]=[]
            specname_specvalue[spec_name].append(spec_value)
        else:
            specname_specvalue[spec_name].append(spec_value)

    return classify_info,spename_info,spevalue_info,classify_specname,specname_specvalue








if __name__=='__main__':
  # classify=get_prodict_classify_info('msa_store')[4]['颜色123']
  # print(classify)
  # print(get_prodict_classify_info('msa_store'))


    #print(get_product_info_by_type('msa_store','lqx', 'NORMAL_PRODUCT'))
  # db_name='msa_store'
  tenant_code='lqx'
  product_type='NORMAL_PRODUCT'
  #
  # product=get_product_info_by_type(db_name,tenant_code, product_type)
  # print(product)
  connect = DbConnect('msa_store')
  product_res = connect.query("SELECT a.product_id,b.id FROM"
                              "(SELECT DISTINCT product_id FROM  store_product_relationship  WHERE store_type= 'ONLINE_STORE' AND product_type =\'" + product_type + "\' AND tenant_code = \'" + tenant_code + "\')  AS a LEFT JOIN  product_sku AS b ON a.product_id = b.product_id")
  print(product_res)
  for product_id,sku_id in product_res:
      print(product_id,sku_id)
