import logging
import chapter_6
import pytest


@pytest.fixture
def my_example_fixture():
    return ((4, 2), 2)


@pytest.fixture
def my_example_fixture_yield():
    a = 4
    b = 2
    c = 2
    yield ((a, b), c)
    a = 0
    b = 0
    c = 0


def func(a, b):
    return a / b


def test_func():
    assert func(4, 2) == 2


def test_func_error():
    with pytest.raises(ZeroDivisionError):
        func(2, 0)


@pytest.mark.parametrize("input, expected", [((4, 2), 2), ((0, 1), 0)])
def test_func_param(input, expected):
    assert func(input[0], input[1]) == expected


def test_func_fix(my_example_fixture):
    input, expected = my_example_fixture
    assert func(input[0], input[1]) == expected


"""
Kalkulator 
Dodawać n liczb
Odejmować n liczb
Dzielić dwie liczby
Mnożyć dwie liczby
Potęgować
Liczyć obwód dowolnej podanej figury 
mszymczyk1@sii.pl

"""
