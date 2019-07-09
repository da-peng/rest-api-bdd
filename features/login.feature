@login
Feature: 登录
  # Enter feature description here

  Scenario Outline: 将登录后的token持久化至文件
    Given 访问登录接口 /auth/open/system/auth/login
    Given <role>账号<account>和<password>
    Then 持久化存储token
    Examples: test
      | account     | password | role     |
      # 测试环境 C端B端账号
      | 15013300167 | wxpud123 | consumer |
      | lqx         | abc123   | manager  |
      # 测试环境，创建的时候用这个管理员账号： lqx
#      | lqx         | abc123   |
      # uat环境