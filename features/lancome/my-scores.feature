# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-我的游戏成绩

  Scenario Outline: 小黑瓶游戏-我的游戏成绩
    Given 请求我的游戏成绩接口/online-game-rankings/my-scores
    Given 我的游戏成绩接口参数<mixNick>&&<gameType>
    Examples:
      | mixNick                                         | gameType            |
      | t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= | LITTLE_BLACK_BOTTLE |
#      | d01FFAbiNvDJ8FgBYFOoJT8ePftTwZSpTqrzWGv5A1FrJM= | LITTLE_BLACK_BOTTLE |