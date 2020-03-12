# Created by grabby at 2020/3/11
Feature: 商品交易数据新增或者更新
  # Enter feature description here
  Scenario: 商品交易数据新增或者更新
    Given 商品交易数据新增或者更新接口/data/api/{tenantCode}/product-deal-datas/save-or-update
    When 读取product-deal-datas数据文件，完成数据组装
    Then 断言statusCode===20000