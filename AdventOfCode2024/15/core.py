from models import ObjectType, Movement, Position
from game_map import GameMap

####################################################################################################
####                                           PT 1                                             ####
####################################################################################################


def apply_movements(game_map: GameMap, movements: list[Movement]):
    old_robot_pos = game_map.get_robot_position()

    for movement in movements:
        old_robot_pos = push_object(game_map, old_robot_pos, movement)


def push_object(
    game_map: GameMap,
    object_position: Position,
    movement: Movement,
) -> Position:
    object_type = game_map.check_position(object_position)
    match movement:
        case Movement.RIGHT:
            new_object_pos = object_position.add_y(1)
        case Movement.DOWN:
            new_object_pos = object_position.add_x(1)
        case Movement.LEFT:
            new_object_pos = object_position.add_y(-1)
        case Movement.UP:
            new_object_pos = object_position.add_x(-1)

    new_position_object = game_map.check_position(new_object_pos)

    if new_position_object == ObjectType.WALL:
        return object_position

    game_map.set_object(new_object_pos, object_type)
    game_map.set_object(object_position, ObjectType.EMPTY)

    return new_object_pos
