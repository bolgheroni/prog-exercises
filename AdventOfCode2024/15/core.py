from models import ElementType, Movement, Position
from game_map import GameMap

####################################################################################################
####                                           PT 1                                             ####
####################################################################################################


def apply_movements(game_map: GameMap, movements: list[Movement]):
    old_robot_pos = game_map.get_robot_position()

    for movement in movements:
        old_robot_pos = push_element(game_map, old_robot_pos, movement)


def push_element(
    game_map: GameMap,
    element_position: Position,
    movement: Movement,
) -> Position:
    element = game_map.check_position(element_position)
    match movement:
        case Movement.RIGHT:
            new_element_pos = element_position.add_y(1)
        case Movement.DOWN:
            new_element_pos = element_position.add_x(1)
        case Movement.LEFT:
            new_element_pos = element_position.add_y(-1)
        case Movement.UP:
            new_element_pos = element_position.add_x(-1)

    new_position_element = game_map.check_position(new_element_pos)

    if new_position_element == ElementType.WALL:
        return element_position

    game_map.set_element(new_element_pos, element)
    game_map.set_element(element_position, ElementType.EMPTY)

    return new_element_pos
