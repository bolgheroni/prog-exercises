from src.marathon import Marathon


def make_sut(
    participants=None
):
    _participants = participants if participants != None else list([
        ('John Doe', 30),
        ('Jane Doe', 25)
    ])
    return Marathon(
        participants=_participants
    )


class TestMarathonCurrentState():
    def test_displays_participants_data(self):
        participants = [
            ('John Doe', 30),
            ('Jane Doe', 25)
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