from src.app_input_collector import AppInputCollector

def make_sut(
        mock_input
):
    return AppInputCollector(
        input_channel=mock_input
    )

def test_collects_action_input():
    sut = make_sut(
        mock_input=lambda message: "1" if "enter the action: " in message.lower() else ""
    )
    assert sut.collect_action_input() == 1

def test_collects_create_type_input():
    sut = make_sut(
        mock_input=lambda message: "truck" if "enter the transport type: " in message.lower() else ""
    )
    assert sut.collect_create_type_input() == "truck"

def test_collects_id_input():
    sut = make_sut(
        mock_input=lambda message: "1" if "enter the transport id: " in message.lower() else ""
    )
    assert sut.collect_id_input() == 1