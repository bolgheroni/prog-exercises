from game_map import RowsGameMap
from models import ObjectType, Movement, Position
from core import apply_movements


def test_single_linear_movement():
    gm = RowsGameMap(
        [
            [ObjectType.ROBOT, ObjectType.EMPTY],
        ]
    )

    movements = [Movement.RIGHT]

    expected_pos = Position(0, 1)
    apply_movements(gm, movements)

    robot_pos = gm.get_robot_position()

    assert robot_pos == expected_pos


def test_multiple_linear_movement():
    gm = RowsGameMap(
        [
            [
                ObjectType.ROBOT,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
        ]
    )

    movements = [Movement.RIGHT, Movement.RIGHT, Movement.RIGHT, Movement.RIGHT]

    expected_pos = Position(0, 4)
    apply_movements(gm, movements)

    robot_pos = gm.get_robot_position()

    assert robot_pos == expected_pos


def test_multiple_bilinear_movement():
    gm = RowsGameMap(
        [
            [
                ObjectType.ROBOT,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
        ]
    )

    movements = [
        Movement.RIGHT,
        Movement.DOWN,
        Movement.LEFT,
        Movement.RIGHT,
        Movement.UP,
    ]

    expected_pos = Position(0, 1)
    apply_movements(gm, movements)

    robot_pos = gm.get_robot_position()

    assert robot_pos == expected_pos


def test_against_wall():
    gm = RowsGameMap(
        [
            [
                ObjectType.WALL,
                ObjectType.WALL,
                ObjectType.WALL,
            ],
            [
                ObjectType.WALL,
                ObjectType.ROBOT,
                ObjectType.WALL,
            ],
            [
                ObjectType.WALL,
                ObjectType.WALL,
                ObjectType.WALL,
            ],
        ]
    )

    movements = [
        Movement.RIGHT,
        Movement.DOWN,
        Movement.LEFT,
        Movement.RIGHT,
        Movement.UP,
    ]
    starting_pos = gm.get_robot_position()
    apply_movements(gm, movements)

    robot_pos = gm.get_robot_position()

    assert robot_pos == starting_pos


def test_pushes_box():
    gm = RowsGameMap(
        [
            [
                ObjectType.ROBOT,
                ObjectType.BOX,
                ObjectType.EMPTY,
            ],
        ]
    )

    print(gm)

    movements = [
        Movement.RIGHT,
    ]
    expected_robot_pos = Position(0, 1)
    expected_box_pos = Position(0, 2)

    apply_movements(gm, movements)

    assert gm.check_position(expected_robot_pos) == ObjectType.ROBOT
    assert gm.check_position(expected_box_pos) == ObjectType.BOX
