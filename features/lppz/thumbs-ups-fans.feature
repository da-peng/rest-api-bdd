Feature: 点赞好友列表

  Scenario Outline:
    Given 访问点赞好友列表接口/{tenantCode}/thumbs-ups/fans
    When 输入混淆昵称<mixNick>&页码<pageNum>&每页大小<pageSize>
    Then 断言点赞好友列表接口访问成功

    Examples:
      | mixNick                                         | pageNum | pageSize |
      |t01wOCuTUaovrlmpm62Dhxp2Lv9XsO5gA7hZ+91xlFG3/Y= | 1       | 15       |