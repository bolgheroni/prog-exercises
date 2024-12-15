from game_map import RowsGameMap
from models import ObjectType, Movement, Position
from core import apply_movements


def test_push_double_box_right():
    gm = RowsGameMap(
        [
            [
                ObjectType.ROBOT,
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
            ],
        ]
    )

    movements = [Movement.RIGHT]

    expected_positions = [
        [Position(0, 0), ObjectType.EMPTY],
        [Position(0, 1), ObjectType.ROBOT],
        [Position(0, 2), ObjectType.BOX_L],
        [Position(0, 3), ObjectType.BOX_R],
    ]
    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type


def test_push_double_box_left():
    gm = RowsGameMap(
        [
            [
                ObjectType.EMPTY,
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.ROBOT,
            ],
        ]
    )

    movements = [Movement.LEFT]

    expected_positions = [
        [Position(0, 0), ObjectType.BOX_L],
        [Position(0, 1), ObjectType.BOX_R],
        [Position(0, 2), ObjectType.ROBOT],
        [Position(0, 3), ObjectType.EMPTY],
    ]
    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type


def test_push_double_box_up_from_left():
    gm = RowsGameMap(
        [
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
            ],
            [
                ObjectType.ROBOT,
                ObjectType.EMPTY,
            ],
        ]
    )

    movements = [Movement.UP]

    expected_positions = [
        [Position(0, 0), ObjectType.BOX_L],
        [Position(0, 1), ObjectType.BOX_R],
        [Position(1, 0), ObjectType.ROBOT],
        [Position(1, 1), ObjectType.EMPTY],
        [Position(2, 0), ObjectType.EMPTY],
        [Position(2, 1), ObjectType.EMPTY],
    ]
    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type


def test_push_double_box_up_from_right():
    gm = RowsGameMap(
        [
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.ROBOT,
            ],
        ]
    )

    movements = [Movement.UP]

    expected_positions = [
        [Position(0, 0), ObjectType.BOX_L],
        [Position(0, 1), ObjectType.BOX_R],
        [Position(1, 0), ObjectType.EMPTY],
        [Position(1, 1), ObjectType.ROBOT],
        [Position(2, 0), ObjectType.EMPTY],
        [Position(2, 1), ObjectType.EMPTY],
    ]
    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type


def test_push_stacked_double_boxes_up():
    gm = RowsGameMap(
        [
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.ROBOT,
            ],
        ]
    )

    movements = [Movement.UP]

    expected_positions = [
        [Position(0, 0), ObjectType.BOX_L],
        [Position(0, 1), ObjectType.BOX_R],
        [Position(1, 0), ObjectType.BOX_L],
        [Position(1, 1), ObjectType.BOX_R],
        [Position(2, 0), ObjectType.EMPTY],
        [Position(2, 1), ObjectType.ROBOT],
        [Position(3, 0), ObjectType.EMPTY],
        [Position(3, 1), ObjectType.EMPTY],
    ]
    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type


def test_push_stacked_double_boxes_up_not_aligned():
    gm = RowsGameMap(
        [
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.ROBOT,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
        ]
    )

    movements = [Movement.UP]

    expected_positions = [
        [Position(0, 0), ObjectType.BOX_L],
        [Position(0, 1), ObjectType.BOX_R],
        [Position(1, 0), ObjectType.BOX_L],
        [Position(1, 1), ObjectType.BOX_R],
        [Position(1, 2), ObjectType.BOX_L],
        [Position(1, 3), ObjectType.BOX_R],
        [Position(2, 1), ObjectType.BOX_L],
        [Position(2, 2), ObjectType.BOX_R],
        [Position(3, 2), ObjectType.ROBOT],
    ]

    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type, f"{position}"


def test_blocked_push_stacked_double_boxes_up_not_aligned():
    gm = RowsGameMap(
        [
            [
                ObjectType.WALL,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.BOX_L,
                ObjectType.BOX_R,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
            [
                ObjectType.EMPTY,
                ObjectType.EMPTY,
                ObjectType.ROBOT,
                ObjectType.EMPTY,
                ObjectType.EMPTY,
            ],
        ]
    )

    movements = [Movement.UP]

    expected_positions = [
        [Position(1, 0), ObjectType.BOX_L],
        [Position(1, 1), ObjectType.BOX_R],
        [Position(2, 0), ObjectType.BOX_L],
        [Position(2, 1), ObjectType.BOX_R],
        [Position(2, 2), ObjectType.BOX_L],
        [Position(2, 3), ObjectType.BOX_R],
        [Position(3, 1), ObjectType.BOX_L],
        [Position(3, 2), ObjectType.BOX_R],
        [Position(4, 2), ObjectType.ROBOT],
    ]
    apply_movements(gm, movements)

    for position, obj_type in expected_positions:
        assert gm.check_position(position) == obj_type, f"{position}"
