# Created by grabbywu at 6/11/19
@group
Feature: 开团/参团操作
  # Enter feature description here

  Scenario Outline: 开团
    Given 访问开团接口 /consumer/{tenant_code}/group/start-instance
#    Given 访问开团接口 /consumer/lqx/group/start-instance
    Given 开团用户及活动信息<wechatAccountId>&<purchases>&<addressId>
    Then  拿到paymentOrderCode和orderid
    Given 访问订单状态接口 /order/{tenant_code}/sale-orders/{orderId}/update-payment-status 并构建参数请求<userId>
#    Then 断言
    Examples: 开团用户及活动信息
      | userId  | wechatAccountId | purchases | addressId |
      # uat
      | 7755722 | 1721            | 1         | 657       |
      #test
#      | 34775784 | 268            | 1         | 881       |
#    Examples: 订单信息
#      | userId  |
#      | 7755722 |
