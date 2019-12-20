# encoding=utf-8
from behave import *
from utils.base_http import BaseHttp
import random
import re

postByToken = BaseHttp().postByToken


@Given(u"访问商品创建接口 {path}")
def step_impl(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = ''.join(path_list)
    context.url = context.host + path

    # db_store = 'msa_store'
    # db_marketing = 'msa_marketing'
    # context.url = context.host + path
    # context.db_marketing = context.db_prefix + db_marketing
    # context.db_store = context.db_prefix + db_store
    # 免费
    # 按件
    # 按重量


@Given(u'商品信息{deliveryType}&{productname}')
def step_impl(context, deliveryType, productname):
    saleStock = 999
    salePrice = 10
    tagPrice = 99
    productVideo_id = 527
    skuCode = ''.join(random.sample('123456789', 9))
    #deliveryType：商品配送类型
    response = postByToken(
        {
            "productDetail": {
                "remark": "<p>有灵魂的商品</p>"
            },
            "deliveryType": deliveryType,

            "freightTemplateId": 126,
            "productSkuList": [{
                "productSkuSpecificationList": [{
                    "specificationName": "分类规格名称-A",
                    "specificationNameId": 106,
                    "specificationValueId": 355,
                    "specificationValue": "规格值1"
                }, {
                    "specificationName": "分类规格名称-B",
                    "specificationNameId": 107,
                    "specificationValueId": 360,
                    "specificationValue": "规格值2"
                }],
                "imageUrl": "https://aliyun-oss-msa.meizhidev.com/templates/20190719/8568aad0ddfb2b19cb3e0aacad89a7c5/0",
                "skuCode": skuCode,
                "saleStock": saleStock,
                "salePrice": salePrice,
                "tagPrice": tagPrice,
                # 是否应用该SKU
                "usable": False
            }],
            "productName": productname,
            "productUnitId": 1,
            "productUnitName": "kg",
            "productDigest": "商品卖点摘要",
            "productImageList": [{
                "imgUrl": "https://aliyun-oss-msa.meizhidev.com/templates/20190719/7d0132e1ade6a3d41e68b3376466821c/0",
                "mainFlag": "YES",
                "useFlag": "YES",
                "sort": 99
            }],
            "productVideo": {
                "id": productVideo_id,
                "url": "https://aliyun-oss-msa.meizhidev.com/templates/20190628/7676f14a2ef68c6e29bbe712cd6f8b85",
                "materialType": "VEDIO",
                "videoCoverImgUrl": "https://aliyun-oss-msa.meizhidev.com/templates/20190628/1ffa2771a162b1f3231d2a5b3bb34389/0"
            },
            "memberDiscountFlag": "YES",
            "deductingStockModel": "ORDER_PAY",

            "productBrandId": 30,
            "productBrandName": "林清轩",

            "productClassifyId": 264,
            "productClassifyName": "A-测试商品分类",

            "videoId": productVideo_id,
            "productType": "NORMAL_PRODUCT"
        }
        , context.url
        , 'manager'
    )
    context.responseContent = str(response['responseContent'])


@Given(u'访问发布商品接口{path}')
def step_impl(context, path):
    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code

    path = ''.join(path_list)
    context.url = context.host + path + context.responseContent

    postByToken([{
        "storeType": "ONLINE_STORE",
        "productSaleStatus": "YES"
    }], context.url, 'manager'
    )
