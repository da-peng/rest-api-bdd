Feature: 微信小程序登录

  Scenario Outline: 微信小程序登录
    Given 访问微信小程序登录接口/auth/open/lqx/auth/adbot-mp-01/wechat-mp-login，输入参数<code>,<inviteCode>
    Then 断言微信小程序登录接口请求成功

    Examples:
      | code                             | inviteCode  |
      | 0432U6Ug2GKn4D0crLTg2WfbUg22U6U9 | 10048626889 |