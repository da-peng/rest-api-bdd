@Login
Feature: 登录
  # Enter feature description here
  @LoginSuccess
  Scenario Outline: 成功登录并获取token
    Given 访问登录接口 /auth/open/system/auth/login
    Given <role>账号<account>和<password>
    Then 断言statusCode===20000
    Then 持久化存储token

    @test
    Examples: Test环境
      | account     | password | role     |
      # 测试环境 C端B端账号
      | lqx         | abc123   | manager  |
    @uat
    Examples: Uat环境
      | account     | password | role     |
      # 测试环境 C端B端账号
      | 15013300167 | wxpud123 | manager  |
      # 测试环境，创建的时候用这个管理员账号： lqx
#      | lqx         | abc123   |
      # uat环境

#  behave --tags=@develop features/tagged_examples.feature