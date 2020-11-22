from behave import given, when, then


@given('Android is reset.')
def reset(context):
    context.reset_status = True


@when('we ask the android about something.')
def do_something(context):
    pass


@then('android replies.')
def replies(context):
    assert True


