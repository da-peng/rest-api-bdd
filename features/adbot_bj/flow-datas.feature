# Created by grabby at 2020/3/11
Feature: 流量数据指标类型新增或者更新
  # Enter feature description here
  Scenario: 流量数据指标类型新增或者更新
    Given 流量数据指标类型新增或者更新接口/data/api/{tenantCode}/flow-datas/save-or-update
    When 读取flow-datas数据文件，完成数据组装
    Then 断言statusCode===20000