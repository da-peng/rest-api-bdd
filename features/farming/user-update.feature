# Created by grabby at 2020/4/23
Feature: 更新

  Scenario Outline: 更新
    Given 更新用户信息接口/user/update
    When 更新用户信息接口参数<uid>&<nick>&<avatar>

    Examples:
      | uid | nick | avatar        |
      | 1   | 哈哈   | www.baidu.com |