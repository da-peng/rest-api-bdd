# Created by grabby at 2020/3/11
Feature: 门店流水概览记录新增或者更新（每天一条）
  # Enter feature description here
  Scenario: 门店流水概览记录新增或者更新（每天一条）
    Given 门店流水概览记录新增或者更新/data/api/{tenantCode}/channel-shop-general-record-day-statistics/save-or-update
    When 读取channel-shop-general-record-day-statistics数据文件，完成数据组装
    Then 断言statusCode===20000