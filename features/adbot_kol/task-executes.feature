Feature:  任务执行详情
  Scenario Outline: :  任务执行详情
    Given 访问任务执行详情接口/consumer/{tenantCode}/task-executes/get/<id>
    Then 断言任务执行详情接口请求成功

    Examples:
    |id|
    | 59 |