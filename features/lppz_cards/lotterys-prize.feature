Feature: 获取抽奖奖品

  Scenario Outline:
    Given 访问获取我的奖品接口/{tenantCode}/lotterys/prize
    When 请输入混淆昵称<mixNick>
    Then 断言获取我的奖品接口访问成功

    Examples:
      | mixNick                                         |
      | aa |