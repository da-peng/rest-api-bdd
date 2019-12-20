Feature: 领取优惠券

  Scenario Outline:
    Given 访问兑奖接口/{tenantCode}/lotterys/exchange，输入混淆昵称<mixNick>&奖品类型<type>&奖品记录ID<prizeId>
#    奖品类型，GIFT_BOX-吴亦凡同款坚果礼盒，SWEATER-潮流合伙人定制卫衣，NECKLACE-潮流合伙人定制项链
    Then 断言兑奖成功

    Examples:
      | mixNick | type    |
      | aa      | GIFT_BOX |