Feature: 获取我的集卡

  Scenario Outline:
    Given 访问开始游戏接口/{tenantCode}/lotterys/play
    When 请输入混淆昵称<mixNick>
    Then 断言开始游戏成功

    Examples:
      | mixNick                                         |
      | aa |