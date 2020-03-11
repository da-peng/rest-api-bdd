# Created by grabby at 2020/3/11
Feature: 品牌列表
  # Enter feature description here

  Scenario Outline: 品牌列表
    Given 访问品牌列表接口/boss/api/system/brands/list
    When 参数<pageNum>&<pageSize>
    Then 断言ResponseContent->list不为空

    Examples:
      | pageNum | pageSize |
      | 1       | 30       |
