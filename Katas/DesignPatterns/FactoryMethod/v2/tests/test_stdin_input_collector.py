from io import StringIO
from src.stdin_input_collector import StdinInputCollector

def make_sut(
        mock_input
):
    return StdinInputCollector(
        input_channel=mock_input
    )

def test_collects_distance():
    sut = make_sut(
        mock_input=lambda message: "100" if "distance" in message else None
    )
    distance = sut.collect_distance()
    assert distance == 100

def test_collects_crew_amount():
    sut = make_sut(
        mock_input=lambda message: "55" if "crew" in message else None
    )
    crew_amount = sut.collect_crew_amount()
    assert crew_amount == 55