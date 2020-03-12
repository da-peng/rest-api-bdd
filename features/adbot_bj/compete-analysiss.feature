# Created by grabby at 2020/3/11
Feature: 竞对分析指标类型新增或者更新
  # Enter feature description here
  Scenario: 竞对分析指标类型新增或者更新
    Given 竞对分析指标类型新增或者更新接口/data/api/{tenantCode}/compete-analysiss/save-or-update
    When 读取compete-analysiss数据文件，完成数据组装
    Then 断言statusCode===20000