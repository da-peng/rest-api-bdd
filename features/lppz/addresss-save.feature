Feature: 新增收货地址

  Scenario Outline:
    Given 访问新增收货地址接口/{tenantCode}/addresss/save
    When 输入混淆昵称<mixNick>&用户名<userName>&手机号<mobile>详细地址<fullAddress>
    Then 断言新增收货地址成功

    Examples:
      | mixNick                                         | userName | mobile      | fullAddress      |
      | d01FFAbiNvDJ8FgBYFOoJT8ePftTwZSpTgrzfJhjA1FrJF= | 丁宁       | 15539541686 | 东北省黑龙江市莲花县池水沟60号 |

