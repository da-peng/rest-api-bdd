Feature: 判断是否获得过相关金币

  Scenario Outline:
    Given 访问判断是否获得过金币接口/{tenantCode}/gold-coin-judges/check
    When 请输入混淆昵称<mixNick>
    Then 断言判断是否获得过相关金币接口访问成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |