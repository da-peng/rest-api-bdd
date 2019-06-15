@login
Feature: 登录
  # Enter feature description here

  Scenario Outline: 将登录后的token持久化至文件
    Given 访问登录接口 /auth/open/system/auth/login
    Given 账号<account>和<password>
    Then 持久化存储token
    Examples: test
      | account     | password |
      | 15013300167 | wxpud123 |
      # 测试环境
#      | lqx         | abc123   |