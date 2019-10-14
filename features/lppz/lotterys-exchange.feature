Feature: 领取优惠券

  Scenario Outline:
    Given 访问领取优惠券接口/{tenantCode}/lotterys/exchange，输入混淆昵称<mixNick>&奖品id<prizeId>&奖品类型<type>
    #类型，STORE-店铺优惠券，PRODUCT-商品优惠券
    Then 断言领取优惠券成功

    Examples:
      | mixNick                                         | prizeId |type|
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= | 16017   | PRODUCT  |