Feature: 获取金币数量

  Scenario Outline:
    Given 访问获取金币数量接口/{tenantCode}/gold-coins/get-gold-coins
    When 请输入混淆昵称<mixNick>
    Then 断言访问获取金币数量接口成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |