from game_map import RowsGameMap
from models import ElementType, Position


def test_single_position_get():
    gm = RowsGameMap([[ElementType.BOX]])

    zero_pos = gm.check_position(Position(0, 0))

    assert zero_pos == ElementType.BOX


def test_single_position_set():
    gm = RowsGameMap([[ElementType.BOX]])

    gm.set_element(Position(0, 0), ElementType.WALL)

    zero_pos = gm.check_position(Position(0, 0))

    assert zero_pos == ElementType.WALL


def test_single_get_robot_position():
    gm = RowsGameMap([[ElementType.ROBOT]])

    robot_pos = gm.get_robot_position()

    assert robot_pos == Position(0, 0)
