Feature: Przelewy

  Background: Logowanie
    Given Zaloguj się

  Scenario: Sprawdź stan konta
    Given Jestem na stronie głównej
    When Klikam w stan konta
    Then Widzę stan konta

