# Created by grabby at 2020/3/11
Feature: 团购详情指标类型新增或者更新
  # Enter feature description here
  Scenario: 团购详情指标类型新增或者更新
    Given 团购详情指标类型新增或者更新接口/data/api/{tenantCode}/group-details/save-or-update
    When 读取group-details数据文件，完成数据组装
    Then 断言statusCode===20000