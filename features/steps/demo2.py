from behave import given, when, then


@given('{objects} are nearby.')
def nearby(context, objects):
    print(objects)


@when('a {error_type} error occurs.')
def error_occurs(context, error_type):
    print(error_type)


@when('android gets {something}.')
def gets_something(context, something):
    print(something)


@when('{objects} cross android field of view.')
def cross_field_of_view(context, objects):
    print(objects)


@then('{objects} is detected.')
def detected(context, objects):
    print(objects)
    assert True


@then('{objects} is not detected.')
def not_detected(context, objects):
    print(objects)
    assert True


@then(u'android turn itself off.')
def turn_off(context):
    assert True
