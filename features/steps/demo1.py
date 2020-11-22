from behave import given, when, then
from android import Android

@given('Android is reset.')
def reset(context):
    context.my_android = Android()
    context.my_android.reset()


@when('we ask the android about something.')
def do_something(context):
    context.my_android.listen('What is your name?')


@then('android replies.')
def replies(context):
    assert context.my_android.speaking() == 'My name is C3PO'


