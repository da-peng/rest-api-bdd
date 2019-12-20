Feature: 获取收货地址

  Scenario Outline:
    Given 访问获取收货地址接口/{tenantCode}/addresss/get-by-mixnick
    When 请输入混淆昵称<mixNick>
    Then 断言获取收货地址成功

    Examples:
      | mixNick                                         |
      | d01FFAbiNvDJ8FgBYFOoJT8ePftTwZSpTgrzfJhjA1FrJF= |