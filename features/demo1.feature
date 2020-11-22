Feature: Test Android behaviour

  Background: Prepare device for test
    Given Android is reset.
    And android is set to test mode.

  @dev
  Scenario: Check if android can speak.
    Given android has mouth.
    When we ask the android about something.
    Then android replies.

  Scenario Outline: Check if android can <move>.
    Given android has <body_part>.
    When android ask to <move>.
    Then android is <move>ing.

    Examples: Moves
      | move | body_part |
      | jump | legs      |
      | grab | arms      |

