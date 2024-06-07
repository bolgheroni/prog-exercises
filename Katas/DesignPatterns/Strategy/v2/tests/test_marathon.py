from src.marathon import Marathon

def make_sut():
    return Marathon()

def test_marathon_current_state():
    def test_displays_participants_data():
        sut = make_sut()
        sut.add_participant('John Doe', 30)
        sut.add_participant('Jane Doe', 25)
        current_state = sut.current_state()

        assert 'John Doe' in current_state
        assert 'Jane Doe' in current_state
        assert '30' in current_state
        assert '25' in current_state

    test_displays_participants_data()