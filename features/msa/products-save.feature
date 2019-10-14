@Product
Feature: 商品
  # Enter feature description here
  @CreateSuccess
  Scenario Outline:
    Given 访问商品创建接口 /store/{tenant_code}/products/save
    Given 商品信息<deliveryType>&<productname>
    Given 访问发布商品接口/store/{tenant-code}/products-store/save-sale-status/

  @test
    Examples: Test环境
      | deliveryType | productname |
      | ALL      | 910商品1    |

  @uat
    Examples: Uat环境
      | deliveryType | productname |
      | EXPRESS      | 商品灵魂        |
      # 测试环境 C端B端账号


      # 测试环境，创建的时候用这个管理员账号： lqx
#      | lqx         | abc123   |
      # uat环境

#  behave --tags=@develop features/tagged_examples.feature