Feature: 获取抽奖奖品

  Scenario Outline:
    Given 访问获取抽奖奖品接口/{tenantCode}/lotterys/prize
    When 请输入混淆昵称<mixNick>
    Then 断言获取抽奖奖品接口访问成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |