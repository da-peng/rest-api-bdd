# Created by grabby at 2020/3/11
Feature: 团购核销单新增或者更新
  # Enter feature description here
  Scenario: 团购核销单新增或者更新
    Given 团购核销单新增或者更新接口/data/api/{tenantCode}/channel-groupon-verification-orders/save-or-update
    When 读取channel-groupon-verification-orders数据文件，完成数据组装
    Then 断言statusCode===20000