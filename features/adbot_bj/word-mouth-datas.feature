# Created by grabby at 2020/3/11
Feature: 口碑数据新增或者更新接口
  # Enter feature description here
  Scenario: 口碑数据新增或者更新接口
    Given 口碑数据新增或者更新接口接口/data/api/{tenantCode}/word-mouth-datas/save-or-update
    When 读取word-mouth-datas数据文件，完成数据组装
    Then 断言statusCode===20000