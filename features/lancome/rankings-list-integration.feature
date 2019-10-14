Feature: 分数相同排名，先玩的排前


#  Scenario Outline: 分数相同排名
#    Given 获取第一名的分数和混淆昵称, 参数<gameType>
#    Then <mixNick>提交游戏结果
#    Then 断言变动后的排行榜第一名的信息
#
#    Examples:
#      | gameType            | mixNick                                         |
#      | LITTLE_BLACK_BOTTLE | 景01yaxl+ahIBfiHvJtEYIN0rqSqzTBhMwYb5P3UFPgULTo= |
#
#
#  Scenario Outline: 排行榜前三名获奖凭证验证
#    Given 断言昨天<gameDate>的排行榜，前三名，有没有获奖凭证
#
#    Examples:
#      | gameDate |
#      | 20190809 |


  Scenario Outline: 假数据验证1
    Given 获取<gameDate>游戏排名
#    Then <mixNick1>提交数据<gamePoint1>
#    Given 获取<gameDate>游戏排名
#    Then <mixNick2>提交数据<gamePoint2>
#    Given 获取<gameDate>游戏排名

    Examples:

      | gameDate | gamePoint1 | gamePoint2 | mixNick1 | mixNick2 |
      | 20190812 | 40         | 41         | aa       | bb       |

#  Scenario Outline: 假数据验证2
#    Given 获取<gameDate>游戏排名
#    Then <mixNick1>提交数据<gamePoint1>
#    Given 获取<gameDate>游戏排名
#    Then <mixNick2>提交数据<gamePoint2>
#    Given 获取<gameDate>游戏排名
#
#    Examples:
#      | gameDate | gamePoint1 | gamePoint2 | mixNick1 | mixNick2 |
#      | 20190810 | 40         | 40         | cc       | dd       |

