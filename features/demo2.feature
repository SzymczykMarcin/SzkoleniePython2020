Feature: Test more Android behaviour

  Background: Prepare device for test
    Given Android is reset.

  Scenario: Check if android has safety mechanism.
    Given android is set to safe mode.
    And humans are nearby.
    When a fatal error occurs.
    Then android turn itself off.

  Scenario: Check if android has object detection implemented.
    Given android has eyes.
    * children are nearby.
    * animals are nearby.
    When child cross android field of view.
    Then child is detected.
    But animal is not detected.


  Scenario: Check if android can eat.
    Given android has mouth.
    When android gets apple.
    Then android is eating.