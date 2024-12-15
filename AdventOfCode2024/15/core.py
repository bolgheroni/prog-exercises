from models import ElementType, Movement
from game_map import GameMap

####################################################################################################
####                                           PT 1                                             ####
####################################################################################################


def apply_movements(game_map: GameMap, movements: list[Movement]):
    old_robot_pos = game_map.get_robot_position()

    for movement in movements:
        new_robot_pos = old_robot_pos.add_y(1)

        game_map.set_element(new_robot_pos, ElementType.ROBOT)
        game_map.set_element(old_robot_pos, ElementType.EMPTY)

        old_robot_pos = new_robot_pos
