@Product
Feature: 商品
  # Enter feature description here
  @CreateSuccess
  Scenario Outline:
    Given 访问商品创建接口 /store/{tenant_code}/products/save
    Given 商品信息<productBrandId>&<productClassifyId>&<freightTemplateId>&<deliveryType>
    Then 断言statusCode===20000
    Then 持久化存储token

    @test
    Examples: Test环境
      | account     | password | role     |
      # 测试环境 C端B端账号
      | 15013300167 | wxpud123 | consumer |
      | lqx         | abc123   | manager  |
    @uat
    Examples: Uat环境
      | account     | password | role     |
      # 测试环境 C端B端账号
      | 15013300167 | wxpud123 | consumer |
      | 15013300167 | wxpud123 | manager  |
      # 测试环境，创建的时候用这个管理员账号： lqx
#      | lqx         | abc123   |
      # uat环境

#  behave --tags=@develop features/tagged_examples.feature