from typing import List, Sequence
import sys
from models import Stone


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


def main(file_path: str):
    data = get_input(file_path)
    print(data)


if __name__ == "__main__":
    file_path = sys.argv[1]

    main(file_path)
