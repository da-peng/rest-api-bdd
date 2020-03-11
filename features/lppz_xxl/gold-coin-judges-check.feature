Feature: 判断是否获得过相关金币

  Scenario Outline:
    Given 访问判断是否获得过相关游戏接口/{tenantCode}/gold-coin-judges/check
    When 请输入混淆昵称<mixNick>
    Then 断言判断是否获得过相关游戏成功

    Examples:
      | mixNick |
      | aa      |