Feature: 赚金币

  Scenario Outline:
    Given 访问赚取抽卡机会接口/{tenantCode}/gold-coins/add
#    SIGN_IN-签到（每天），FOLLOR-关注旗舰店（一次性），MEMBER-成为会员（一次性），SHARE-分享（每天2次）
    When 输入任务类型<sourceType>&混淆昵称<mixNick>
    Then 断言赚取抽卡机会接口访问成功

    Examples:
      | sourceType | mixNick |
      | SIGN_IN    | aa      |
