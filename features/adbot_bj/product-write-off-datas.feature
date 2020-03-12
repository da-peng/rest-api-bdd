# Created by grabby at 2020/3/11
Feature: 商品核销数据新增或者更新
  # Enter feature description here
  Scenario: 商品核销数据新增或者更新
    Given 商品核销数据新增或者更新接口/data/api/{tenantCode}/product-write-off-datas/save-or-update
    When 读取product-write-off-datas数据文件，完成数据组装
    Then 断言statusCode===20000