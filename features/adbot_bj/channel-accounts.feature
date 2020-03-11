# Created by grabby at 2020/3/11
Feature: 品牌渠道账号信息获取

  Scenario Outline: 品牌渠道账号信息获取
    Given 访问品牌渠道账号信息获取/boss/api/system/channel-accounts/list
    When 品牌渠道账号信息参数<pageNum>&<pageSize>&<brandCode>&<channelCode>
    Then 断言ResponseContent->list不为空

    Examples: 数据
      | pageNum | pageSize | brandCode | channelCode |
      | 1       | 30       | aiweiting | MEI_DIAN     |
