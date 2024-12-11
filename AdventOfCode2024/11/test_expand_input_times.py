from models import Stone
from solution import expand_input_times


def test_expand_input_once():
    input_list = [
        Stone(125),
        Stone(17),
    ]

    result = expand_input_times(input_list, 1)

    assert result == [Stone(253000), Stone(1), Stone(7)]


def test_expand_input_times_2():
    input_list = [
        Stone(125),
        Stone(17),
    ]

    result = expand_input_times(input_list, 2)

    assert result == [253, 0, 2024, 14168]


def test_expand_input_times_6():
    input_list = [
        Stone(125),
        Stone(17),
    ]

    result = expand_input_times(input_list, 6)

    assert result == [
        2097446912,
        14168,
        4048,
        2,
        0,
        2,
        4,
        40,
        48,
        2024,
        40,
        48,
        80,
        96,
        2,
        8,
        6,
        7,
        6,
        0,
        3,
        2,
    ]


def test_expand_input_times_25():
    input_list = [
        Stone(125),
        Stone(17),
    ]

    result = expand_input_times(input_list, 25)

    assert len(result) == 55312
