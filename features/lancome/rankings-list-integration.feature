Feature: 分数相同排名，后玩的排前

  Scenario Outline: 分数相同排名
    Given 获取第一名的分数和混淆昵称, 参数<gameType>
    Then <mixNick>提交游戏结果
    Then 断言变动后的排行榜第一名的信息

    Examples:
       | gameType            |mixNick|
       | LITTLE_BLACK_BOTTLE |  aa   |