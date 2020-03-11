Feature: 获取活动时间

  Scenario:
    Given 访问获取活动时间接口/{tenantCode}/lotterys/activity-time
    When 简单FROM_GET请求
    Then 断言获取活动时间接口访问成功
