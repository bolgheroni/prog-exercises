from src.handlers.handlers_chain import HandlersChain
from tests.fake_handler import FakeHandler
from src.models.order import Order

def test_calls_first_handler():
    first_handler = FakeHandler()

    sut = HandlersChain()
    sut.add_handler(first_handler)

    order = Order()

    sut.handle(order)

    assert first_handler.handle_called_with(order) == True
    

    


