# Created by grabbywu at 6/10/19
@Group
Feature: 拼团测试
  @CreateGroupSuccess
#  Background:
  Scenario Outline: 创建拼团
    Given 访问创建拼团活动接口 /marketing/{tenant_code}/activity-group/create
#    Given 访问创建拼团活动接口 /marketing/baiyang/activity-group/create
    Given 创建<n>个活动；活动信息<product_type>&<groupDurationHours>&<groupCompletePeoples>&<activityProductLimit>
#    Then 持久化存储活动名称
    Then 断言statusCode===20000
    @test
    Examples: 拼团活动信息 Test环境
      | n  | product_type   | groupDurationHours | groupCompletePeoples | activityProductLimit |
      | 10 | NORMAL_PRODUCT | 2                  | 10                   | 2                    |
    @uat
    Examples: 拼团活动信息 Uat环境
      | n  | product_type   | groupDurationHours | groupCompletePeoples | activityProductLimit |
      | 10 | NORMAL_PRODUCT | 2                  | 10                   | 2                    |

