Feature:  评论详情同步
  # Enter feature description here
  Scenario:  评论详情同步
    Given  评论详情同步接口/data/api/{tenantCode}/shop-reviews/save-or-update
    When 读取shop-reviews数据文件，完成数据组装
    Then 断言statusCode===20000

  #channel_shop_code   varchar(64)              not null comment '渠道门店编码',
  #review_id           varchar(128)             not null comment '评论ID',
