from typing import Dict, List, Sequence
import sys
from models import Stone, get_expansion_code


def get_input(file_path: str) -> List[int]:
    with open(file_path, "r") as file:
        line = file.readline()
        return [int(x) for x in line.split(" ")]


def expand_once(stone: Stone) -> Sequence[Stone]:
    if stone == Stone(0):
        return [stone + 1]

    str_stone = str(stone)
    digits_amount = len(str_stone)

    if digits_amount % 2 != 0:
        return [Stone(2024 * stone)]

    left_digits = str_stone[: int(digits_amount / 2)]
    right_digits = str_stone[int(-digits_amount / 2) :]

    return [Stone(left_digits), Stone(right_digits)]


def expand_times(stone: Stone, times: int) -> Sequence[Stone]:
    expanded_once_sequence = expand_once(stone)
    if times == 1:
        return expanded_once_sequence

    result = []

    for expanded_stone in expanded_once_sequence:
        full_branch = expand_times(expanded_stone, times - 1)
        result.extend(full_branch)

    return result


def expand_times_size_with_cache(
    stone: Stone, times: int, cache: Dict[str, int]
) -> int:
    expansion_code = get_expansion_code(stone=stone, times=times)
    cached_response = cache.get(expansion_code)
    if cached_response is not None:
        return cached_response

    expanded_once_sequence = expand_once(stone)
    if times == 1:
        response = len(expanded_once_sequence)
        cache[expansion_code] = response

        return response

    response = 0

    for expanded_stone in expanded_once_sequence:
        response += expand_times_size_with_cache(
            stone=expanded_stone, times=times - 1, cache=cache
        )
        cache[expansion_code] = response

    return response


def expand_input_times(input_data: Sequence[Stone], times: int):
    result = []
    for stone in input_data:
        result.extend(expand_times(stone, times))

    return result


def expand_input_times_size_with_cache(input_data: Sequence[Stone], times: int) -> int:
    cache = dict()
    result = 0
    for stone in input_data:
        result += expand_times_size_with_cache(stone=stone, times=times, cache=cache)

    return result


def main(file_path: str, times: int):
    data = get_input(file_path)

    expanded_lenght = expand_input_times_size_with_cache(input_data=data, times=times)
    print(f"Expanded length: {expanded_lenght}")


if __name__ == "__main__":
    file_path = sys.argv[1]
    times = sys.argv[2]

    main(file_path, int(times))
