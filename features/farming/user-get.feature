# Created by grabby at 2020/4/23
Feature: 获取用户信息

  Scenario Outline: 获取用户信息
    Given 获取用户信息接口/user/get
    When 获取用户信息接口参数<uid>

    Examples:
      | uid |
      | 1   |