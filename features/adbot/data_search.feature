Feature: 数据检索
  Scenario Outline:
    Given 访问数据检索接口/data/{tenantCode}/data-search/list-page
    When 输入参数<domain>&<username>
    Then 搜索成功

    Examples:
      |domain|username|
      |weibo|鞠婧祎|
