Feature: 点赞排行

  Scenario Outline:
    Given 访问点赞排行接口/{tenantCode}/thumbs-ups/ranking
    When 输入获取条数<limit>
    Then 断言点赞排行接口访问成功

    Examples:
      | limit |
      |   10 |