from v2.src.ship_transport import ShipTransport

def make_sut(
    crew_amount: int = 10,
    distance_km: int = 1000,
    id: int = 1
):
    return ShipTransport(
        crew_amount=crew_amount,
        distance_km=distance_km,
        id=id
    )

def test_ship_transport_eta():
    sut = make_sut(
        distance_km=1000,
        crew_amount=100
    )
    eta = sut.eta()
    
    assert eta.hours == 37
    assert eta.minutes == 2
    

