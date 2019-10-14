Feature: 点赞

  Scenario Outline:
    Given 访问点赞接口/{tenantCode}/thumbs-ups/save/<userId>
    When 输入点赞人混淆昵称<mixNickFans>
    Then 断言点赞成功

    Examples:
      | mixNickFans | userId |
      | love         | 5      |