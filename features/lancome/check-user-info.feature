# Created by grabbywu at 2019-08-15
Feature:  是否提供过会员名
  # Enter feature description here

  Scenario Outline:  是否提供过会员名
    Given 访问是否提供过会员名接口/bespeak/check-user-info
    Then  是否提供过会员名接口参数<mixNick>

    Examples:
      | mixNick |
      | a       |