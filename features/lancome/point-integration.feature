# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-游戏集成测试(前置条件，以下所有用户之前都未获得加赠券）

  Scenario Outline: 小黑瓶游戏-游戏测试1
    Given <mixNick>获得游戏分数<P1>分
    Then 断言statusCode===20000
    Then 断言还差<S1>分，得到<M1>个加赠券
    Then 断言获得加赠券<N1>张及今日游戏最高分<C1>

    Given <mixNick>获得游戏分数<P2>分
    Then 断言statusCode===20000
    Then 断言还差<S2>分，得到<M2>个加赠券
    Then 断言获得加赠券<N2>张及今日游戏最高分<C2>

    Given <mixNick>获得游戏分数<P3>分
    Then 断言statusCode===20000
    Then 断言还差<S3>分，得到<M3>个加赠券
    Then 断言获得加赠券<N3>张及今日游戏最高分<C3>

    Given <mixNick>获得游戏分数<P4>分
    Then 断言statusCode===20000
    Then 断言获得加赠券<N4>张及今日游戏最高分<C4>


    Examples:
      | mixNick                                         | P1 | N1 | C1 | S1 | M1 | P2 | N2 | C2 | S2 | M2 | P3 | N3 | C3 | S3 | M3 | P4 | N4 | C4 |
      | 司01acVrxu9SNwVI1wv2qGLZVaSqzTBhMwYb5P3UFPgULTo= | 30 | 0  | 30 | 21 | 1  | 31 | 1  | 31 | 10 | 2  | 41 | 2  | 41 | 10 | 3  | 51 | 3  | 51 |


  Scenario Outline: 小黑瓶游戏-游戏测试2
    Given <mixNick>获得游戏分数<P1>分
    Then 断言statusCode===20000
    Then 断言还差<S1>分，得到<M1>个加赠券
    Then 断言获得加赠券<N1>张及今日游戏最高分<C1>

    Given <mixNick>获得游戏分数<P2>分
    Then 断言statusCode===20000
    Then 断言还差<S2>分，得到<M2>个加赠券
    Then 断言获得加赠券<N2>张及今日游戏最高分<C2>

    Given <mixNick>获得游戏分数<P3>分
    Then 断言statusCode===20000
    Then 断言获得加赠券<N3>张及今日游戏最高分<C3>

    Examples:
      | mixNick                                         | P1 | N1 | C1 | S1 | M1 | P2 | N2 | S2 | M2 | C2 | P3 | N3 | C3 |
      | 华01qe7WRuMPuETxV2rsDX2mTqSqzTBhMwYb5P3UFPgULTo= | 35 | 1  | 35 | 6  | 2  | 31 | 1  | 20 | 2  | 35 | 51 | 3  | 51 |


  Scenario Outline: 小黑瓶游戏-游戏测试3
    Given <mixNick>获得游戏分数<P1>分
    Then 断言statusCode===20000
    Then 断言还差<S1>分，得到<M1>个加赠券
    Then 断言获得加赠券<N1>张及今日游戏最高分<C1>

    Given <mixNick>获得游戏分数<P2>分
    Then 断言statusCode===20000
    Then 断言获得加赠券<N2>张及今日游戏最高分<C2>


    Examples:
      | mixNick                                         | P1 | N1 | C1 | S1 | M1 | P2  | N2 | C2  |
      | d01FFAbiNvDJ8FgBYFOoJT8ePftTwZSpTqrzWGv5A1FrJM= | 41 | 2  | 41 | 10 | 3  | 100 | 3  | 100 |


  Scenario Outline: 小黑瓶游戏-游戏测试4
    Given <mixNick>获得游戏分数<P1>分
    Then 断言statusCode===20000
    Then 断言获得加赠券<N1>张及今日游戏最高分<C1>
    
    Examples:
      | mixNick                                         | P1 | N1 | C1 |
      | 日01dnMspl4ZupGuxlQI4vLebVavOOIexRl9KFi8nZNtFmM= | 51 | 3  | 51 |