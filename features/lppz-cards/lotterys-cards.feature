Feature: 获取我的集卡

  Scenario Outline:
    Given 访问获取我的集卡接口/{tenantCode}/lotterys/cards
    When 请输入混淆昵称<mixNick>
    Then 断言获取我的集卡接口访问成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |