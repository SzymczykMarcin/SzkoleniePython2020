from behave import given, when, then
from android import Android

@given('android is set to {mode}.')
def check_if_set_mode(context, mode):
    context.my_android.set_mode(mode)
    assert context.my_android.mode == mode


@given('android has {body_part}.')
def check_if_has_body_part(context, body_part):
    assert body_part in context.my_android.body_parts


@when('android ask to {move}.')
def ask_to_move(context, move):
    if move == 'jump':
        context.my_android.jump()
    elif move == 'grab':
        context.my_android.grab()

@then('android is {move}ing.')
def moving(context, move):
    assert context.my_android.action == move
