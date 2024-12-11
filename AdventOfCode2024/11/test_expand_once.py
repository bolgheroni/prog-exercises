from models import Stone
from solution import expand_once


def test_zero_stone():
    stone = Stone(0)

    result = expand_once(stone)

    assert result == [Stone(1)]


def test_one_stone():
    stone = Stone(1)

    result = expand_once(stone)

    assert result == [Stone(2024)]


def test_expand_two():
    stone = Stone(2)

    result = expand_once(stone)

    assert result == [Stone(4048)]


# def test_expand_ten():
#     stone = Stone(10)

#     result = expand_once(stone)

#     assert result == [Stone(1), Stone(0)]
