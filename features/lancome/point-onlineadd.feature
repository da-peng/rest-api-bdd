# Created by grabbywu at 2019-08-08
Feature: 小黑瓶游戏-游戏结束调用积分

  Scenario Outline: 小黑瓶游戏-游戏结束调用积分
    Given 请求游戏结束调用积分接口/nascent/point/onlineadd
    Given 游戏结束调用积分接口参数<mixNick>&&<gameType>&&<gameUsedSeconds>&&<gamePoint>
    Examples:
      | mixNick                                         | gameType            | gameUsedSeconds | gamePoint |
      | r014GJTyWc11MVz2oOoURsuXFavOOIexRl9KFi8nZNtFmM= | LITTLE_BLACK_BOTTLE | 10              | 51        |
