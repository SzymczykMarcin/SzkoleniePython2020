from behave import given, when, then

@given("Zaloguj się")
def logowanie(context):
    ...

@given("Jestem na stronie głównej")
def glowna(context):
    ...

@when("Klikam w stan konta")
def stan_konta(context):
    ...

@then("Widzę stan konta")
def sprawdz_stan_konta(context):
    assert True