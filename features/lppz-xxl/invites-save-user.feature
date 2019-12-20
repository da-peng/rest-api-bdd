Feature: 邀请好友

  Scenario Outline:
    Given 访问邀请好友接口/{tenantCode}/invites/save/<userId>
    When 请输入淘宝用户id<userId>&受邀人的混淆昵称<mixNickFans>
    Then 断言邀请好友成功

    Examples:
      | userId |mixNickFans|
      | aa      |          |