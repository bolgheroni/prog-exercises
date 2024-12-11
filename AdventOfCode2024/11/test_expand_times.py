from models import Stone
from solution import expand_times


def test_0_times_1():
    stone = Stone(0)

    result = expand_times(stone=stone, times=1)

    assert result == [Stone(1)]
