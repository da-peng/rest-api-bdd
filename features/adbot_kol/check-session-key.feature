Feature: 检查wechatSessionKey是否有效
  Scenario: 检查wechatSessionKey是否有效
    Given 访问检查wechatSessionKey是否有效接口/auth/noauth/{tenantCode}/check-wechat-account-session-key
    Then 断言检查wechatSessionKey是否有效接口请求成功
