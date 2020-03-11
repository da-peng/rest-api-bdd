Feature: 用户登录
  Scenario Outline:
    Given 访问登录接口/auth/open/system/auth/login
    When 输入账号<username>密码<password>
    Then 登陆成功，持久化存储!

    Examples:
    |username|password|
    |    18898759328    |   abc@123456     |

