Feature: 抽奖

  Scenario Outline:
    Given 访问抽卡接口/{tenantCode}/lotterys/go
    When 输入混淆昵称<mixNick>游戏关卡<gameLevel>游戏关卡<gameScore>
    Then 断言抽卡接口访问成功

    Examples:
      | mixNick |gameLevel|gameScore|
      | aa      |      1   |     1    |