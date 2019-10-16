Feature: 获取游戏排名
  Scenario Outline: : 获取游戏排名
    Given 请求游戏排名接口/online-game-rankings/list
    Given 游戏排名接口参数<gameDate>&<gameType>
    Examples:
    |gameDate        |         gameType          |
    |    20190812    |    LITTLE_BLACK_BOTTLE    |

