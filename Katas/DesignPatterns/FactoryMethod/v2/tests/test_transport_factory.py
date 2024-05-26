from src.transport_factory import TransportFactory
from tests.fake_input_collector import FakeInputCollector

def make_sut(
    input_collector
):
    return TransportFactory(
        input_collector=input_collector
    )

def test_collects_only_distance_for_truck():
    input_collector = FakeInputCollector().set_distance(100).set_crew_amount(54)
    sut = make_sut(
        input_collector
    )
    transport = sut.create_transport(
        id=1,
        type="TRUCK"
    )
    description = str(transport)
    assert "100" in description
    assert "54" not in description
    
def test_collects_crew_amount_and_distance_for_ship():
    input_collector = FakeInputCollector().set_crew_amount(54).set_distance(99)
    sut = make_sut(
        input_collector
    )
    transport = sut.create_transport(
        id=1,
        type="SHIP"
    )
    description = str(transport)
    assert "54" in description
    assert "99" in description


