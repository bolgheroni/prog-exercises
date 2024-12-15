from game_map import RowsGameMap
from models import ElementType, Movement, Position
from core import apply_movements


def test_single_linear_movement():
    gm = RowsGameMap(
        [
            [ElementType.ROBOT, ElementType.EMPTY],
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
                ElementType.ROBOT,
                ElementType.EMPTY,
                ElementType.EMPTY,
                ElementType.EMPTY,
                ElementType.EMPTY,
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
                ElementType.ROBOT,
                ElementType.EMPTY,
            ],
            [
                ElementType.EMPTY,
                ElementType.EMPTY,
            ],
            [
                ElementType.EMPTY,
                ElementType.EMPTY,
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
                ElementType.WALL,
                ElementType.WALL,
                ElementType.WALL,
            ],
            [
                ElementType.WALL,
                ElementType.ROBOT,
                ElementType.WALL,
            ],
            [
                ElementType.WALL,
                ElementType.WALL,
                ElementType.WALL,
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
