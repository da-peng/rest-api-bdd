# Created by grabby at 2020/3/11
Feature:  推广通计划流水新增(每天一条)
  # Enter feature description here
  Scenario:  推广通计划流水新增(每天一条)
    Given  推广通计划流水新增接口/data/api/{tenantCode}/channel-extension-programme-record-day-statistics/save-or-update
    When 读取channel-extension-programme-record-day-statistics数据文件，完成数据组装
    Then 断言statusCode===20000