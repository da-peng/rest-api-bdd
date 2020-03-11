# Created by grabby at 2020/3/11
Feature: 评论新增或者更新
  # Enter feature description here

  Scenario: 评论新增或者更新
    Given 评论新增或者更新接口/data/api/{tenantCode}/channel-comment/save-or-update
    When 读取channel-comment数据文件，完成数据组装
    Then 断言statusCode===20000
