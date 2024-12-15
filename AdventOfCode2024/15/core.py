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
            target_pos = object_position.add_y(1)
        case Movement.DOWN:
            target_pos = object_position.add_x(1)
        case Movement.LEFT:
            target_pos = object_position.add_y(-1)
        case Movement.UP:
            target_pos = object_position.add_x(-1)

    next_object = game_map.check_position(target_pos)

    if next_object == ObjectType.WALL:
        return object_position

    if next_object == ObjectType.BOX:
        pushed_next_object_position = push_object(game_map, target_pos, movement)
        is_next_object_stuck = pushed_next_object_position == target_pos
        if is_next_object_stuck:
            return object_position

    if next_object == ObjectType.BOX_L and movement == Movement.RIGHT:
        # push right side first
        box_r_position = target_pos.add_y(1)
        pushed_box_r_position = push_object(game_map, box_r_position, movement)
        is_r_stuck = pushed_box_r_position == box_r_position

        if is_r_stuck:
            return object_position
        else:
            # now push left side
            push_object(game_map, target_pos, movement)

    if next_object == ObjectType.BOX_R and movement == Movement.LEFT:
        # push left side first
        box_l_position = target_pos.add_y(-1)
        pushed_box_l_position = push_object(game_map, box_l_position, movement)
        is_l_stuck = pushed_box_l_position == box_l_position

        if is_l_stuck:
            return object_position
        else:
            # now push right side
            push_object(game_map, target_pos, movement)

    game_map.set_object(target_pos, object_type)
    game_map.set_object(object_position, ObjectType.EMPTY)

    return target_pos
