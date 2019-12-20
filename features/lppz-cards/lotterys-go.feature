Feature: 抽奖

  Scenario Outline:
    Given 访问抽卡接口/{tenantCode}/lotterys/go，混淆昵称<mixNick>
#    When 请输入混淆昵称<mixNick>
    Then 断言抽卡接口访问成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |