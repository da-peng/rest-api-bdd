# Created by grabby at 2020/4/23
Feature: 注册

  Scenario Outline: 注册
    Given 注册接口/register
    When 参数<username>&<password>

    Examples:
      | username | password |
      | test     | 1        |