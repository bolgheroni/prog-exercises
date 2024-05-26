from io import StringIO
from src.app import App
from src.truck_transport import TruckTransport
from tests.fake_transports_control import FakeTransportsControl
from tests.fake_input_collector import FakeInputCollector

def make_sut(
    output_channel=None,
    input_collector=None,
    transports_control=None
):
    _output_channel = output_channel if output_channel else StringIO()
    _input_collector = input_collector if input_collector else FakeInputCollector().set_action_input("0")
    _transports_control = transports_control if transports_control else FakeTransportsControl().set_transports_list([])

    return App(
        output_channel=_output_channel,
        input_collector=_input_collector,
        transports_control=_transports_control
    )

def test_displays_actions_list():
    mock_output = StringIO()
    sut = make_sut(
        output_channel=mock_output
    )
    sut.loop()
    actions_list = mock_output.getvalue()
    assert "1 - List transports" in actions_list
    assert "2 - Create transport" in actions_list
    assert "3 - Deploy transport" in actions_list
    assert "4 - Exit" in actions_list

def test_displays_empty_transports_list():
    input_collector = FakeInputCollector().set_action_input("1")
    mock_output = StringIO()
    sut = make_sut(
        input_collector=input_collector,
        output_channel=mock_output
    )
    sut.loop()

    assert "No transports available" in mock_output.getvalue()


def test_collects_user_input():
    input_collector = FakeInputCollector().set_action_input("1")
    mock_output = StringIO()
    sut = make_sut(
        input_collector=input_collector,
        output_channel=mock_output
    )
    sut.loop()

    assert "Current Transports List" in mock_output.getvalue()


def test_displays_transports_list():
    # arrange
    input_collector = FakeInputCollector().set_action_input("1")
    mock_output = StringIO()
    truck1 = TruckTransport(
        id=99,
        distance_km=65
    )
    fake_transports_control = FakeTransportsControl().set_transports_list([truck1])
    sut = make_sut(
        input_collector=input_collector,
        output_channel=mock_output,
        transports_control=fake_transports_control
    )
    # act
    sut.loop()

    # assert
    assert "65" in mock_output.getvalue()
    assert "TRUCK" in mock_output.getvalue()
    assert "99" in mock_output.getvalue()

def test_creates_transport():
    # arrange
    input_collector = FakeInputCollector().set_action_input("2").set_create_type_input("TRUCK").set_id_input("99")
    mock_output = StringIO()
    fake_transports_control = FakeTransportsControl().set_transports_list([])

    sut = make_sut(
        input_collector=input_collector,
        output_channel=mock_output,
        transports_control=fake_transports_control
    )

    # act
    sut.loop()

    # assert
    assert fake_transports_control.called_create_transport(
        type="TRUCK",
        id=99
    )
    
def test_deploys_transport():
    # arrange
    input_collector = FakeInputCollector().set_action_input("3").set_id_input("99")
    mock_output = StringIO()
    transport = TruckTransport(
        id=99,
        distance_km=65
    )
    fake_transports_control = FakeTransportsControl().set_transports_list([
        transport
    ])

    sut = make_sut(
        input_collector=input_collector,
        output_channel=mock_output,
        transports_control=fake_transports_control
    )

    # act
    sut.loop()

    # assert
    assert fake_transports_control.called_deploy_transport(
        id=99
    )

def test_should_exit():
    # arrange
    input_collector = FakeInputCollector().set_action_input("4")
    mock_output = StringIO()
    sut = make_sut(
        input_collector=input_collector,
        output_channel=mock_output
    )

    # act
    sut.loop()

    # assert
    assert sut.should_exit() == True