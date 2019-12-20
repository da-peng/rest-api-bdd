Feature: 赚取游戏机会

  Scenario Outline:
    Given 访问赚取游戏机会接口/{tenantCode}/gold-coins/add
#   SIGN_IN-签到（每天），FOLLOR-关注旗舰店（一次性），MEMBER-成为会员（一次性），SHARE-邀请好友，WELL_WISHING-发送新年祝福
    When 输入任务类型<sourceType>&混淆昵称<mixNick>&新年祝福<wellWishing>
    # 新年祝福，sourceType=WELL_WISHING时必需
    Then 断言赚取抽卡机会接口访问成功

    Examples:
      | sourceType | mixNick |wellWishing|
      | SIGN_IN    | aa      |     1      |
