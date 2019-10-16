Feature: 修改收货地址

  Scenario Outline:
    Given 访问修改收货地址接口/{tenantCode}/addresss/update
    When 输入混淆昵称<mixNick>&用户名<userName>&手机号<mobile>详细地址<fullAddress>
    Then 断言修改收货地址成功

    Examples:
      | mixNick                                         | userName | mobile      | fullAddress  |
      | d01FFAbiNvDJ8FgBYFOoJT8ePftTwZSpTgrzfJhjA1FrJF= | 大宁       | 15539541685 | 河南省漯河市丁湾村70号 |