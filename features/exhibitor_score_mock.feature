# Created by grabbywu at 4/24/19
Feature: 模拟展商游戏结果
  # Enter feature description here

  Scenario: 模拟展商返回游戏分数结果
    Given 访问接口 /lancome/nascent/point/add
    Given 请求参数：混淆昵称及积分
    |taobaoId|point|
    |111111  |20   |