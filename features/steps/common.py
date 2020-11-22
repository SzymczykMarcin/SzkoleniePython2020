from behave import given, when, then


@given('android is set to {mode}.')
def set_mode(context, mode):
    print(context.reset_status)


@given('android has {body_part}.')
def set_mode(context, body_part):
    print(body_part)


@when('android ask to {move}.')
def ask_to_move(context, move):
    print(move)


@then('android is {move}ing.')
def moving(context, move):
    print(move)
    assert True
