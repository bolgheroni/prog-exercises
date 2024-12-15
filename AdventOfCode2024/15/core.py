from models import ElementType, Movement
from game_map import GameMap

####################################################################################################
####                                           PT 1                                             ####
####################################################################################################


def apply_movements(game_map: GameMap, movements: list[Movement]):
    old_robot_pos = game_map.get_robot_position()

    for movement in movements:
        match movement:
            case Movement.RIGHT:
                new_robot_pos = old_robot_pos.add_y(1)
            case Movement.DOWN:
                new_robot_pos = old_robot_pos.add_x(1)
            case Movement.LEFT:
                new_robot_pos = old_robot_pos.add_y(-1)
            case Movement.UP:
                new_robot_pos = old_robot_pos.add_x(-1)

        if game_map.check_position(new_robot_pos) == ElementType.WALL:
            continue

        game_map.set_element(new_robot_pos, ElementType.ROBOT)
        game_map.set_element(old_robot_pos, ElementType.EMPTY)

        old_robot_pos = new_robot_pos
