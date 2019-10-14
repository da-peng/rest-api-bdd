Feature: 赚金币

  Scenario Outline:
    Given 访问赚金币接口/{tenantCode}/gold-coins/add
    #SIGN_IN-签到（每天），FOLLOR-关注旗舰店（一次性），MEMBER-成为会员（一次性），SHARE-分享（每天5次），COLLECT-收藏商品，ADD_CART加购商品
    When 输入赚金币类型<sourceType>&收藏加购商品<productCode>&混淆昵称<mixNick>
    Then 断言赚取金币成功

    Examples:
      | sourceType | productCode                | mixNick                                         |
      | COLLECT    | 556295961861_4219575808693 | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= |
