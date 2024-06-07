from src.sprint_game import make_sprint_game
from src.participant import Participant
from src.constant_runner import ConstantRunner

def make_sut(
    participants=None,
    distance=None
):
    _participants = participants if participants != None else list([
        Participant(
            name='John Doe',
            age=30
        ),
        Participant(
            name='Jane Doe',
            age=25
        )
    ])
    _distance = distance if distance != None else 200
    return make_sprint_game(
        participants=_participants,
        distance=_distance
    )



class TestMarathonTick():

    def test_finishes_race_after_runner_reaches_200_meters(self):
        participants = [
            Participant(
                name='John Doe',
                age=30,
                action_strategy=ConstantRunner(1)
            ),
        ]
        sut = make_sut(
            participants=participants,
            distance=200
        )
        sut.start()

        for _ in range(200):
            sut.tick()

        current_state = sut.current_state()

        assert 'finished' in current_state.status.lower()

