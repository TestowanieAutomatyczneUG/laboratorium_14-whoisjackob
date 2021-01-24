Feature: Roman Scenarios

  Scenario Outline:
    Given I am in the zad01 directory
    When the input is <strand1>
    Then the output should be <result>

    Examples:
      |       strand1 |  result |
      |             9 |      IX |
      |            59 |     LIX |
      |          3000 |     MMM |
      |          1024 |   MXXIV |