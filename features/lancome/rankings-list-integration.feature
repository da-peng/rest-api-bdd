Feature: 分数相同排名，先玩的排前

  Scenario Outline: 分数相同排名
    Given 获取第一名的分数和混淆昵称, 参数<gameType>
    Then <mixNick>提交游戏结果
    Then 断言变动后的排行榜第一名的信息

    Examples:
      | gameType            | mixNick                                         |
      | LITTLE_BLACK_BOTTLE | 景01yaxl+ahIBfiHvJtEYIN0rqSqzTBhMwYb5P3UFPgULTo= |


  Scenario Outline: 排行榜前三名获奖凭证验证
    Given 断言昨天<gameDate>的排行榜，前三名，有没有获奖凭证

    Examples:
      | gameDate |
      | 20190809 |
  Scenario Outline: : 获得过获奖凭证的会员不能再次获得
     Given <gameDate1>获得过优惠券
     Then <gameDate2>,依然是前三名,不会获得优惠券
     Examples:
       |gameDate1|gameDate2|
       |    20190809   |     20190812     |