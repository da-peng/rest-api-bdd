# Created by grabby at 2020/4/27
Feature: 获取蔬菜价格

  Scenario Outline: 获取蔬菜价格
    Given 获取蔬菜价格接口/vegetable/price
    When 获取蔬菜价格接口参数<vegetable>&<startTime>&<endTime>

    Examples:
      | vegetable | startTime           | endTime             |
      | 矮脚白菜      | 2020-04-20 08:00:00 | 2020-04-26 23:59:59 |