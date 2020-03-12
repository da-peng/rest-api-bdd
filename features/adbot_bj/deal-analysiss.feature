# Created by grabby at 2020/3/11
Feature: 交易分析指标类型新增或者更新
  # Enter feature description here
  Scenario: 交易分析指标类型新增或者更新
    Given 交易分析指标类型新增或者更新接口/data/api/{tenantCode}/deal-analysiss/save-or-update
    When 读取deal-analysiss数据文件，完成数据组装
    Then 断言statusCode===20000