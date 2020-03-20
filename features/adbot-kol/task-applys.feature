Feature: kol报名任务
  Scenario Outline: kol报名任务
    Given 访问kol报名任务接口/consumer/{tenantCode}/task-applys/save-apply/<taskId>
    When 输入参数<taskStoreId>,<taskProjectId>
    Then 断言kol报名任务接口请求成功

    Examples:
    #taskId 任务ID taskStoreId任务门店ID 选择项目ID
    |taskId|taskStoreId|taskProjectId|
    |   3   |      2     |      1       |


