# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-获取奖励凭证

  Scenario Outline: 小黑瓶游戏-获取奖励凭证
    Given 请求获取奖励凭证接口/game-prizes/get-by-mixnick
    Given 获取奖励凭证接口参数<mixNick>&&<gameType>
    Examples:
      | mixNick                                         | gameType            |
      | 司01acVrxu9SNwVI1wv2qGLZVaSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE |
      | 华01qe7WRuMPuETxV2rsDX2mTqSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE |