from typing import Dict
from models import Stone
from solution import expand_times_size_with_cache


def test_0_times_1():
    stone = Stone(0)
    cache: Dict[str, int] = {"0#1": 7}

    cached_result = expand_times_size_with_cache(stone=stone, times=1, cache=cache)

    assert cached_result == 7

    clean_result = expand_times_size_with_cache(stone=stone, times=1, cache=dict())
    assert clean_result == 1


# def test_0_times_2():
#     stone = Stone(0)

#     result = expand_times(stone=stone, times=2)

#     assert result == [Stone(2024)]


# def test_0_times_3():
#     stone = Stone(0)

#     result = expand_times(stone=stone, times=3)

#     assert result == [Stone(20), Stone(24)]


# def test_0_times_4():
#     stone = Stone(0)

#     result = expand_times(stone=stone, times=4)

#     assert result == [Stone(2), Stone(0), Stone(2), Stone(4)]
