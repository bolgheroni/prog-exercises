from models import Stone
from solution import expand_once


def test_zero_stone():
    stone = Stone(0)

    result = expand_once(stone)

    assert result == Stone(1)
