# Created by grabbywu at 2019-08-15
Feature: 新增或修改淘宝用户信息
  # Enter feature description here

  Scenario Outline: 新增或修改淘宝用户信息
    Given 访问新增或修改淘宝用户信息接口/bespeak/save-user-info
    Then 新增或修改淘宝用户信息接口参数<mixNick>&&<nick>

    Examples:
      | mixNick | nick |
      | a       | a    |