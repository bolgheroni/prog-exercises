from game_map import RowsGameMap
from models import ObjectType, Position


def test_single_position_get():
    gm = RowsGameMap([[ObjectType.BOX]])

    zero_pos = gm.check_position(Position(0, 0))

    assert zero_pos == ObjectType.BOX


def test_single_position_set():
    gm = RowsGameMap([[ObjectType.BOX]])

    gm.set_object(Position(0, 0), ObjectType.WALL)

    zero_pos = gm.check_position(Position(0, 0))

    assert zero_pos == ObjectType.WALL


def test_single_get_robot_position():
    gm = RowsGameMap([[ObjectType.ROBOT]])

    robot_pos = gm.get_robot_position()

    assert robot_pos == Position(0, 0)


def test_multiple_check_position():
    gm = RowsGameMap(
        [
            [ObjectType.WALL, ObjectType.EMPTY, ObjectType.WALL],
            [ObjectType.WALL, ObjectType.EMPTY, ObjectType.WALL],
            [ObjectType.WALL, ObjectType.ROBOT, ObjectType.WALL],
        ]
    )

    pos = gm.check_position(Position(2, 1))

    assert pos == ObjectType.ROBOT


def test_multiple_set_object():
    gm = RowsGameMap(
        [
            [ObjectType.WALL, ObjectType.EMPTY, ObjectType.WALL],
            [ObjectType.WALL, ObjectType.EMPTY, ObjectType.WALL],
            [ObjectType.WALL, ObjectType.ROBOT, ObjectType.WALL],
        ]
    )

    assert gm.check_position(Position(1, 1)) == ObjectType.EMPTY

    gm.set_object(Position(1, 1), ObjectType.WALL)

    assert gm.check_position(Position(1, 1)) == ObjectType.WALL


def test_multiple_get_robot_position():
    gm = RowsGameMap(
        [
            [ObjectType.WALL, ObjectType.EMPTY, ObjectType.WALL],
            [ObjectType.WALL, ObjectType.EMPTY, ObjectType.WALL],
            [ObjectType.WALL, ObjectType.ROBOT, ObjectType.WALL],
        ]
    )

    robot_pos = gm.get_robot_position()

    assert robot_pos == Position(2, 1)
