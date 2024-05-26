from v2.src.transports_control import TransportsControl
from v2.src.transport_factory import TransportFactory
from v2.tests.fake_input_collector import FakeInputCollector

def make_sut(
    input_collector=None
):
    _input_collector = input_collector if input_collector else FakeInputCollector()
    return TransportsControl(
        transport_factory=TransportFactory(
            input_collector=_input_collector
        )
    )

def test_creates_truck():
    sut = make_sut()
    transport = sut.create_transport(
        type="TRUCK",
        id=1
    )
    description = str(transport)
    assert "TRUCK" in description
    assert "1" in description

def test_creates_ship():
    input_collector = FakeInputCollector().set_crew_amount(54)
    sut = make_sut(input_collector)
    transport = sut.create_transport(
        type="SHIP",
        id=1
    )
    description = str(transport)
    assert "SHIP" in description
    assert "1" in description

def test_list_transports_when_empty():
    sut = make_sut()
    assert sut.list_transports() == []

def test_add_transports_to_list():
    input_collector = FakeInputCollector()
    sut = make_sut(input_collector)
    input_collector.set_distance(100)
    sut.create_transport(
        type="TRUCK",
        id=1
    )
    input_collector.set_crew_amount(200)
    sut.create_transport(
        type="SHIP",
        id=2
    )

    transports_list = sut.list_transports() 

    assert len(transports_list) == 2
    
    truck_description = str(transports_list[0])
    assert "TRUCK" in truck_description
    assert "1" in truck_description

    ship_description = str(transports_list[1])
    assert "SHIP" in ship_description
    assert "2" in ship_description

def test_deploys_transport():
    sut = make_sut()
    transport = sut.create_transport(
        type="TRUCK",
        id=1
    )

    assert transport.is_deployed() == False
    description = str(transport)
    assert "not deployed" in description.lower()
    
    sut.deploy_transport(1)
    assert transport.is_deployed() == True

    description = str(transport)
    assert "deployed" in description.lower()
    