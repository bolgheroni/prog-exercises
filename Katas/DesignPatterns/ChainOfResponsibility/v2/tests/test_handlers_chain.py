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
    
def test_calls_second_handler():
    first_handler = FakeHandler().with_valid_order()
    second_handler = FakeHandler().with_valid_order()

    sut = HandlersChain()
    sut.add_handler(first_handler)
    sut.add_handler(second_handler)

    order = Order()

    sut.handle(order)

    assert first_handler.handle_called_with(order) == True
    assert second_handler.handle_called_with(order) == True
    

def test_returns_none_if_handlers_are_empty():
    sut = HandlersChain()

    order = Order()

    result = sut.handle(order)

    assert result == None

def test_removes_first_handler_by_index():
    first_handler = FakeHandler().with_valid_order()
    second_handler = FakeHandler().with_valid_order()

    sut = HandlersChain()
    sut.add_handler(first_handler)
    sut.add_handler(second_handler)

    order = Order()

    sut.remove_handler(0)

    sut.handle(order)

    assert first_handler.handle_called_with(order) == False
    assert second_handler.handle_called_with(order) == True