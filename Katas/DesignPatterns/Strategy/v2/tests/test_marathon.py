from src.marathon import create_marathon
from src.participant import Participant
from src.states.participant_state import ParticipantState
from src.constant_runner import ConstantRunner

def make_sut(
    participants=None
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
    return create_marathon(
        participants=_participants
    )


class TestMarathonCurrentState():
    def test_displays_participants_data(self):
        participants = [
            Participant(
                name='John Doe',
                age=30,
                state=ParticipantState(10)
            ),
            Participant(
                name='Jane Doe',
                age=25,
                state=ParticipantState(1)
            )
        ]
        sut = make_sut(
            participants=participants
        )
        current_state = sut.current_state()
        participants_state = current_state.participants.lower()

        assert 'john doe' in participants_state
        assert 'jane doe' in participants_state
        assert '30' in participants_state
        assert '25' in participants_state
        assert '10' in participants_state
        assert '1' in participants_state

    def test_displays_empty_participants_data(self):
        sut = make_sut(
            participants=[]
        )
        current_state = sut.current_state()

        assert 'no participants' in current_state.participants.lower()

    def test_displays_race_status(self):
        sut = make_sut()
        current_state = sut.current_state()

        assert 'not started' in current_state.status.lower()

        sut.start()

        current_state = sut.current_state()

        assert 'in progress' in current_state.status.lower()

    def test_displays_ticks_since_start(self):
        sut = make_sut()

        sut.start()

        current_state = sut.current_state()

        assert current_state.ticks == 0

        sut.tick()

        current_state = sut.current_state()

        assert current_state.ticks == 1

    def test_displays_winner_when_finished(self):
        participants = [
            Participant(
                name='John Doe',
                age=30,
                state=ParticipantState(0)
            )
        ]
        sut = make_sut(
            participants=participants
        )
        sut.start()

        participants[0].state.position = 40000

        sut.tick()

        current_state = sut.current_state()

        assert 'finished' in current_state.status.lower()
        assert participants[0] in current_state.winners


class TestMarathonStart():
    def test_resets_participants_state(self):
        participants = [
            Participant(
                name='John Doe',
                age=30
            ),
        ]
        sut = make_sut()
        sut.start()

        assert participants[0].state.position == 0


class TestMarathonTick():
    def test_increases_ticks(self):
        sut = make_sut()
        sut.start()

        assert sut.ticks == 0

        sut.tick()

        assert sut.ticks == 1

    def test_updates_participants_state(self):
        participants = [
            Participant(
                name='John Doe',
                age=30,
                action_strategy=ConstantRunner(1)
            ),
            Participant(
                name='Jane Doe',
                age=25,
                action_strategy=ConstantRunner(2)
            )
        ]
        sut = make_sut(
            participants=participants
        )
        sut.start()

        start_positions = [participants[0].state.position,
                           participants[1].state.position]

        sut.tick()

        assert participants[0].state.position == start_positions[0] + 1
        assert participants[1].state.position == start_positions[1] + 2

    def test_finishes_race_after_runner_reaches_40000_meters(self):
        participants = [
            Participant(
                name='John Doe',
                age=30,
                action_strategy=ConstantRunner(1)
            ),
        ]
        sut = make_sut(
            participants=participants
        )
        sut.start()

        for _ in range(40000):
            sut.tick()

        current_state = sut.current_state()

        assert 'finished' in current_state.status.lower()

    def test_when_is_finished_throws_error(self):
        sut = make_sut()
        sut.start()

        for _ in range(40000):
            sut.tick()

        try:
            sut.tick()
            assert False
        except Exception as e:
            message = str(e).lower()

            assert 'finished' in message

    def test_when_is_not_started_throws_error(self):
        sut = make_sut()

        try:
            sut.tick()
            assert False
        except Exception as e:
            message = str(e).lower()

            assert 'started' in message