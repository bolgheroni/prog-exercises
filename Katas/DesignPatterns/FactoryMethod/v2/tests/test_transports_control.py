from v2.src.transports_control import TransportsControl

def make_sut():
    return TransportsControl()

def test_creates_truck():
    sut = make_sut()
    transport = sut.create_transport(
        type="TRUCK",
        id=1
    )
    assert transport.id == 1
    assert transport.type == "TRUCK"

def test_creates_ship():
    sut = make_sut()
    transport = sut.create_transport(
        type="SHIP",
        id=1
    )
    assert transport.id == 1
    assert transport.type == "SHIP"

def test_list_transports_when_empty():
    sut = make_sut()
    assert sut.list_transports() == []

def test_add_transports_to_list():
    sut = make_sut()
    sut.create_transport(
        type="TRUCK",
        id=1
    )
    sut.create_transport(
        type="SHIP",
        id=2
    )

    transports_list = sut.list_transports() 

    assert len(transports_list) == 2
    
    assert transports_list[0].id == 1
    assert transports_list[0].type == "TRUCK"

    assert transports_list[1].id == 2
    assert transports_list[1].type == "SHIP"


    