Feature: 点赞抽奖集成测试

  Scenario Outline:
    Given 查询当前用户<mixNick>已有金币
    Given <n>个好友为<userId>点赞,获得金币为<m>枚
    Then 抽奖<l>次，剩余金币为<h>枚

    Examples:

      | mixNick                                         | n | userId | m   | l | h   |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= | 4 | 5      | 406 | 10 | 326 |