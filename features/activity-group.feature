# Created by grabbywu at 6/10/19
@group
Feature: 拼团测试
  Scenario Outline: 创建拼团
    Given 访问创建拼团活动接口 /marketing/{tenant_code}/activity-group/create
#    Given 访问创建拼团活动接口 /marketing/baiyang/activity-group/create
    Given 创建<n>个活动；活动信息<product_type>&<groupDurationHours>&<groupCompletePeoples>&<activityProductLimit>
    Then 持久化存储活动名称
    Examples: 测试数据nums
      | n | product_type   | groupDurationHours | groupCompletePeoples | activityProductLimit |
      # 测试环境
#      | 1442      | 1148  | 1                  | 2                    | 10                   |
#      | 1442      | 1148  | 2                  | 2                    | 10                   |
#      | 1442      | 1148  | 2                  | 2                    | 10                   |
      # UAT环境
      | 5 | NORMAL_PRODUCT | 2                  | 3                    | 10                   |

