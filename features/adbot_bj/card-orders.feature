Feature:  次卡订单同步(每天一条)
  # Enter feature description here
  Scenario:  次卡订单同步
    Given  次卡订单同步接口/data/api/{tenantCode}/card-orders/save-or-update
    When 读取card-orders数据文件，完成数据组装
    Then 断言statusCode===20000

    # order_id      varchar(128)      not null comment '订单ID',
