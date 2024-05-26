from v2.src.transport_factory import TransportFactory
from v2.tests.fake_input_collector import FakeInputCollector

def make_sut(
    input_collector
):
    return TransportFactory(
        input_collector=input_collector
    )

def test_collects_distance_for_truck():
    input_collector = FakeInputCollector().set_distance(100)
    sut = make_sut(
        input_collector
    )
    transport = sut.create_transport(
        id=1,
        type="TRUCK"
    )
    description = str(transport)
    assert "100" in description
    



