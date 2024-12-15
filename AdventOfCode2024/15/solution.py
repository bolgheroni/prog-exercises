import sys
from typing import List, Tuple

from models import ObjectType, Movement
from game_map import GameMap, RowsGameMap

####################################################################################################
####                                          Input                                             ####
####################################################################################################


def get_input(
    map_file_path: str, movements_file_path: str
) -> Tuple[GameMap, List[Movement]]:
    with open(map_file_path, "r") as file:
        rows = []
        for line in file.readlines():
            new_row = []

            for col in line:
                if col != "\n":
                    new_row.append(ObjectType(col))

            rows.append(new_row)

    movements = []
    with open(movements_file_path, "r") as file:
        for line in file.readlines():
            for col in line:
                if col != "\n":
                    movements.append(Movement(col))

    return [RowsGameMap(rows=rows), movements]


####################################################################################################
####                                           Main                                             ####
####################################################################################################


def main(map_file_path: str, movements_file_path: str):
    game_map, movements = get_input(
        map_file_path=map_file_path, movements_file_path=movements_file_path
    )

    solution = ""
    # print(f"GameMap: \n\n{game_map}")
    # print(f"Movements: \n\n{movements}")
    print(f"Solution: \n\n{solution}")


if __name__ == "__main__":
    map_file_path = sys.argv[1]
    movements_file_path = sys.argv[2]

    main(map_file_path=map_file_path, movements_file_path=movements_file_path)
