# Created by grabby at 2020/3/11
Feature: 团购退款订单新增
  # Enter feature description here

  Scenario : 团购退款订单新增
    Given 团购退款订单新增接口/data/api/{tenantCode}/channel-groupon-refund-orders/save-or-update
    When 读取channel-groupon-refund-orders数据文件，完成数据组装
    Then 断言statusCode===200