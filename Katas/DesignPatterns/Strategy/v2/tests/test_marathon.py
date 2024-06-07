from src.marathon import Marathon

def make_sut(
    participants=None
):
    _participants = participants or list([
        ('John Doe', 30),
        ('Jane Doe', 25)
    ])
    return Marathon(
        participants=_participants
    )

def test_marathon_current_state():
    def test_displays_participants_data():
        participants = [
            ('John Doe', 30),
            ('Jane Doe', 25)
        ]
        sut = make_sut(
            participants=participants
        )
        current_state = sut.current_state()

        assert 'John Doe' in current_state
        assert 'Jane Doe' in current_state
        assert '30' in current_state
        assert '25' in current_state

    test_displays_participants_data()