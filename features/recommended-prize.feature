# Created by grabbywu at 7/11/19
Feature: 推荐有奖
  Scenario Outline: 创建推荐有奖活动
    Given 访问推荐有奖创建接口 /marketing/{tenant_code}/activity-recommends/create
    Given 创建<n>个推荐有奖活动，活动信息<product_num>&<product_type>
    Then 断言statusCode===20000
    @test
    Examples: product_num 活动商品添加数量
      | n  | product_num | product_type   |
      | 10 | 2           | NORMAL_PRODUCT |
    @uat
    Examples: product_num 活动商品添加数量
      | n  | product_num | product_type   |
      | 10 | 2           | NORMAL_PRODUCT |
