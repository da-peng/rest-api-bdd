Feature:  评论详情同步
  # Enter feature description here
  Scenario:  评论详情同步
    Given  评论详情同步接口/data/api/{tenantCode}/course-orders/save-or-update
    When 读取course-orders数据文件，完成数据组装
    Then 断言statusCode===20000


    # unified_order_id  varchar(64)  not null comment '订单统一编号', update