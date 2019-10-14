Feature: 用户点赞数、当日新增、排名

  Scenario Outline:
    Given 访问用户点赞数、当日新增、排名接口/{tenantCode}/thumbs-ups/me
    When 请输入混淆昵称<mixNick>
    Then 断言用户点赞数、当日新增、排名接口访问成功

    Examples:
      | mixNick                                         |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y=|