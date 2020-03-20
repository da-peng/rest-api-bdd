Feature: kol账号审核

  Scenario Outline: kol账号审核
    Given 访问kol账号审核接口/kol/{tenantCode}/kol-accounts/approval-status/{id},输入参数<kolId>,<approvalRemark>,<approvalStatus>
    Then 断言kol账号审核接口请求成功

    Examples:
    #approvalStatus APPROVALED审核通过,NOAPPROVAL审核不通过
      | kolId | approvalRemark | approvalStatus |
      | 223   | lll            | APPROVALED     |