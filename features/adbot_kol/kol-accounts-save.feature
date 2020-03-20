Feature: kol账号申请

  Scenario Outline: kol账号申请
    Given 访问kol账号申请接口/consumer/{tenantCode}/kol-accounts/save,输入参数<accountLevel>,<gender>
    Then 断言kol账号申请接口请求成功

    Examples:
    #accountLevel 账号等级 gender 性别：MALE-男,FEMALE-女,UNKNOWN-未确定
      | accountLevel | gender |
      | 50           | MALE   |