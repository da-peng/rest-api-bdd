# encoding=utf-8
from behave import *
from utils.time_manage import *
from service.coupon_info import *
from service.product_info import *
from utils.http_util import HttpUtils
from random import *
import re

postByToken = HttpUtils().postByToken

@Given(u"访问商品创建接口 {path}")
def step_impl(context, path):

    path_list = re.split('{|}', path)
    path_list[1] = context.tenant_code
    path = ''.join(path_list)

    # db_store = 'msa_store'
    # db_marketing = 'msa_marketing'
    # context.url = context.host + path
    # context.db_marketing = context.db_prefix + db_marketing
    # context.db_store = context.db_prefix + db_store
# 免费
{
"freightTemplateId": 127,
}
# 按件
{

}

# 按重量
{

}



def step_impl(context,):
    response = postByToken(
        {
            "productDetail": {
                "remark": "<p>商品描述</p>"
            },
            "deliveryType": "EXPRESS",

            "freightTemplateId": 127,
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
                "skuCode": "PRODUCT-SKU0002",
                "saleStock": 999,
                "salePrice": 10,
                "tagPrice": 99,
                #是否应用该SKU
                "usable": false
            }],
            "productName": "测试商品名称",
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
                "id": 527,
                "url": "https://aliyun-oss-msa.meizhidev.com/templates/20190628/7676f14a2ef68c6e29bbe712cd6f8b85",
                "materialType": "VEDIO",
                "videoCoverImgUrl": "https://aliyun-oss-msa.meizhidev.com/templates/20190628/1ffa2771a162b1f3231d2a5b3bb34389/0"
            },
            "memberDiscountFlag": "YES",
            "deductingStockModel": "ORDER_PAY",
            "productBrandId": 54,
            "productBrandName": "测试品牌",
            "productClassifyId": 264,
            "productClassifyName": "A-测试商品分类",
            "videoId": 527,
            "productType": "NORMAL_PRODUCT"
        }
        , context.url
        , 'manager'
    )