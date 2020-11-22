from calculator import dodawanie
import pytest

@pytest.mark.parametrize("input_1, input_2, result", [(1,1,2),(1.5, 1.5, 3), (-1, -1, -2)])
def test_dodawanie(input_1, input_2, result):
    assert dodawanie(input_1, input_2) == result

@pytest.mark.parametrize("input_1, input_2", [([1,2,3], [1,2,3]), ("Ala", "kota"), ("1", "1")])
def test_dodawanie_error(input_1, input_2):
    with pytest.raises(TypeError):
        dodawanie(input_1, input_2)
