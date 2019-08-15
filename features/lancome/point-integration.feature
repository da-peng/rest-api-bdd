# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-游戏集成测试(前置条件，以下所有用户之前都未获得加赠券）

  Scenario Outline: 小黑瓶游戏-（没有一张优惠券）
    Given <mixNick>获得游戏分数<P>分
    Then 断言statusCode===20000
    Then 复活前check游戏分数<C1>,还差<S1>分，得<N1>个加赠券
    Then 复活前check游戏分数<C2>,还差<S2>分，得<N2>个加赠券
    Then 复活前check游戏分数<C3>,还差<S3>分，得<N3>个加赠券
    Then 本场游戏结束提交数据，游戏分数<M>分
    Then 断言获得加赠券<X>张及今日游戏最高分<H>

    Examples:
      | mixNick | P | C1 | S1 | N1 | C2 | S2 | N2 | C3 | S3 | N3 | M  | X | H  |
      | a       | 5 | 9  | 1  | 1  | 10 | 10 | 2  | 20 | 10 | 3  | 21 | 2 | 21 |


  Scenario Outline: 小黑瓶游戏-(已有2张优惠券）
    Given <mixNick>获得游戏分数<P>分
    Then 断言statusCode===20000
    Then 复活前check游戏分数<C1>,还差<S1>分，得<N1>个加赠券
    Then 复活前check游戏分数<C2>,还差<S2>分，得<N2>个加赠券
    Then 复活前check游戏分数<C3>,还差<S3>分，得<N3>个加赠券
    Then 本场游戏结束提交数据，游戏分数<M>分
    Then 断言获得加赠券<X>张及今日游戏最高分<H>

    Examples:
      | mixNick | P  | C1 | S1 | N1 | C2 | S2 | N2 | C3 | S3 | N3 | M  | X | H  |
      | wuli-2  | 22 | 9  | 21 | 1  | 20 | 10 | 1  | 30 | 0  | 0  | 30 | 3 | 30 |


#  Scenario Outline: 小黑瓶游戏-（20，40，50边界）
#    Given <mixNick>获得游戏分数<P>分
#    Then 断言statusCode===20000
#    Then 复活前check游戏分数<C1>,还差<S1>分，得<N1>个加赠券
#    Then 复活前check游戏分数<C2>,还差<S2>分，得<N2>个加赠券
#    Then 复活前check游戏分数<C3>,还差<S3>分，得<N3>个加赠券
#    Then 本场游戏结束提交数据，游戏分数<M>分
#    Then 断言获得加赠券<X>张及今日游戏最高分<H>
#
#    Examples:
#      | mixNick   | P  | C1 | S1 | N1 | C2 | S2 | N2 | C3 | S3 | N3 | M    | X | H    |
#      | test-rfid | 10 | 30 | 1  | 1  | 40 | 1  | 2  | 50 | 1  | 3  | 2000 | 3 | 2000 |