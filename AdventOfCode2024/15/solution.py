import sys
from typing import List, Tuple

from models import Movement
from game_map import EmptyGameMap, GameMap
####################################################################################################
####                                          Input                                             ####
####################################################################################################


def get_input(
    map_file_path: str, movements_file_path: str
) -> Tuple[GameMap, List[Movement]]:
    # with open(map_file_path, "r") as file:
    #     line = file.readline()

    movements = []
    # with open(movements_file_path, "r") as file:
    #     line = file.readline()

    return [EmptyGameMap(), movements]


####################################################################################################
####                                           Main                                             ####
####################################################################################################


def main(map_file_path: str, movements_file_path: str):
    game_map, movements = get_input(
        map_file_path=map_file_path, movements_file_path=movements_file_path
    )

    solution = ""
    print(f"Solution: {solution}")


if __name__ == "__main__":
    map_file_path = sys.argv[1]
    movements_file_path = sys.argv[2]

    main(map_file_path=map_file_path, movements_file_path=movements_file_path)
