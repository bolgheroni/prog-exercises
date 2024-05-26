from src.truck_transport import TruckTransport

def make_sut(
    distance_km: int = 100,
    id: int = 1
):
    return TruckTransport(
        distance_km=distance_km,
        id=id
    )

def test_truck_transport_eta():
    sut = make_sut(
        distance_km=110
    )
    eta = sut.eta()
    assert eta.hours == 2
    assert eta.minutes == 12
    
    description = str(sut)
    assert "2h12m" in description


