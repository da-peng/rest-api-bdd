# Created by grabby at 2020/4/23
Feature: 登录

  Scenario Outline: 登录
    Given 登录接口/login
    When 登录接口参数<username>&<password>

    Examples:
      | username | password |
      | test     | 1        |