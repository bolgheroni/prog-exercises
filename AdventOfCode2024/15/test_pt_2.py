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
