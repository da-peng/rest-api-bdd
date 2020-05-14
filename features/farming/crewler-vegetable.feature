# Created by grabby at 2020/4/27
Feature: 爬虫蔬菜价格
  # Enter feature description here

  Scenario Outline: 爬虫蔬菜价格
    Given 爬虫蔬菜价格接口/crewler/vegetable
    When 爬虫蔬菜价格接口参数<startTime>&<endTime>

    Examples:
      | startTime | endTime  |
      | 2020-04-01  | 2020-04-30 |