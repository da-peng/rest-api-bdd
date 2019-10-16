Feature: 获取幸运值

  Scenario Outline:
    Given 访问获取幸运值接口/{tenantCode}/gold-coins/get-lucks
    When 请输入混淆昵称<mixNick>
    Then 断言获取幸运值成功
    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |