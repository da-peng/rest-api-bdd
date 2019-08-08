# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-还差n分得到m个加赠券

  Scenario Outline:  小黑瓶游戏-还差n分得到m个加赠券
    Given 请求游戏结果判断接口/nascent/point/check
    Given 游戏结果判断接口参数<mixNick>&&<gameType>&&<gameUsedSeconds>&&<gamePoint>
    Examples:
      | mixNick                                         | gameType            | gameUsedSeconds | gamePoint |
      | 司01acVrxu9SNwVI1wv2qGLZVaSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE | 10              | 20        |
      | 华01qe7WRuMPuETxV2rsDX2mTqSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE | 10              | 30        |