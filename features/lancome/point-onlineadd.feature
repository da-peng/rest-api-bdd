# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-游戏结束调用积分

  Scenario Outline: 小黑瓶游戏-游戏结束调用积分
    Given 请求游戏结束调用积分接口/nascent/point/onlineadd
    Given 游戏结束调用积分接口参数<mixNick>&&<gameType>&&<gameUsedSeconds>&&<gamePoint>
    Examples:
      | mixNick                                         | gameType            | gameUsedSeconds | gamePoint |
      | 司01acVrxu9SNwVI1wv2qGLZVaSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE | 10              | 20        |
      | 华01qe7WRuMPuETxV2rsDX2mTqSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE | 10              | 30        |