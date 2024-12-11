from models import Stone
from solution import expand_input_times


def test_expand_once_input():
    input_list = [
        Stone(125),
        Stone(17),
    ]

    result = expand_input_times(input_list, 1)

    assert result == [Stone(253000), Stone(1), Stone(7)]
