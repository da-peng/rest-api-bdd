# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-我的游戏成绩

  Scenario Outline: 小黑瓶游戏-我的游戏成绩
    Given 请求我的游戏成绩接口/online-game-rankings/my-scores
    Given 我的游戏成绩接口参数<mixNick>&&<gameType>
    Examples:
      | mixNick   | gameType            |
      | test-rfid | LITTLE_BLACK_BOTTLE |
#      | 华01qe7WRuMPuETxV2rsDX2mTqSqzTBhMwYb5P3UFPgULTo= | LITTLE_BLACK_BOTTLE |

