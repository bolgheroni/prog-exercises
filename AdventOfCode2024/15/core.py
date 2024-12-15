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

    if new_position_object == ObjectType.BOX:
        pushed_object_position = push_object(game_map, new_object_pos, movement)
        if pushed_object_position == new_object_pos:
            return object_position

    if new_position_object == ObjectType.BOX_L and movement == Movement.RIGHT:
        # push right side first
        pushed_box_r_position = push_object(game_map, new_object_pos.add_y(1), movement)
        is_r_stuck = pushed_box_r_position == new_object_pos.add_y(1)
        if is_r_stuck:
            return object_position
        else:
            push_object(game_map, new_object_pos, movement)

    if new_position_object == ObjectType.BOX_R and movement == Movement.LEFT:
        # push left side first
        pushed_box_l_position = push_object(
            game_map, new_object_pos.add_y(-1), movement
        )
        is_l_stuck = pushed_box_l_position == new_object_pos.add_y(-1)
        if is_l_stuck:
            return object_position
        else:
            push_object(game_map, new_object_pos, movement)

    game_map.set_object(new_object_pos, object_type)
    game_map.set_object(object_position, ObjectType.EMPTY)

    return new_object_pos
