Feature: 获取集赞奖品

  Scenario Outline:
    Given 访问获奖集赞接口/{tenantCode}/thumbs-ups/prize
    When 请输入混淆昵称<mixNick>
    Then 断言获取集赞奖品成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |