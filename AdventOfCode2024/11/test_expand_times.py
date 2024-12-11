from models import Stone
from solution import expand_times


def test_0_times_1():
    stone = Stone(0)

    result = expand_times(stone=stone, times=1)

    assert result == [Stone(1)]


def test_0_times_2():
    stone = Stone(0)

    result = expand_times(stone=stone, times=2)

    assert result == [Stone(2024)]


def test_0_times_3():
    stone = Stone(0)

    result = expand_times(stone=stone, times=3)

    assert result == [Stone(20), Stone(24)]


def test_0_times_4():
    stone = Stone(0)

    result = expand_times(stone=stone, times=4)

    assert result == [Stone(2), Stone(0), Stone(2), Stone(4)]
