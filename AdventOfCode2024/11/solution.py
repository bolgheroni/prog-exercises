from typing import List
import sys
from models import Stone


def get_input(file_path: str) -> List[int]:
    with open(file_path, "r") as file:
        line = file.readline()
        return [int(x) for x in line.split(" ")]


def expand_once(stone: Stone) -> Stone:
    return stone + 1


def main(file_path: str):
    data = get_input(file_path)
    print(data)


if __name__ == "__main__":
    file_path = sys.argv[1]

    main(file_path)
