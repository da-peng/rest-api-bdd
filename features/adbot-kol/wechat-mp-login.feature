Feature: 微信小程序登录

  Scenario Outline: 微信小程序登录
    Given 访问微信小程序登录接口/auth/open/ceshi/auth/adbot-mp-01/wechat-mp-login，输入参数<code>,<inviteCode>
    Then 断言微信小程序登录接口请求成功
    Then 储存微信信息

    Examples:
      | code                             | inviteCode  |
      | 033L6irT17KkQ21UOBpT1k2krT1L6irJ| 10048626889 |