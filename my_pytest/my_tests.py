import pytest

from my_code import passing, adding, division, sinus

from unittest.mock import patch
from math import pi


testdata_adding = [(1, 1, 2), ('a', 'b', 'ab')]

@pytest.fixture
def my_fix():
    a = True
    yield a
    a = False

def test_passing():
    assert passing(1) == 1


@pytest.mark.parametrize("a,b,expected", testdata_adding)
def test_adding(a, b, expected):
    assert adding(a, b) == expected


def test_division():
    with pytest.raises(ZeroDivisionError):
        division(10 / 0)

@patch('my_code.sin', return_value=pi)
def test_sins(mock_sin):
    assert sinus(1) == pi

def test_something(my_fix):
    if my_fix is True:
        assert passing(1) == 1

