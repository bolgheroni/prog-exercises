from src.app import App
from tests.fake_handler import FakeHandler
from src.models.order import Order
from src.handlers.handler import Handler

def make_sut(
    handlers_chain: Handler
):
    app = App(
        handlers_chain=handlers_chain
    )
    return app

def test_pass_order_to_handlers_chain():
    fake_chain = FakeHandler()
    app = make_sut(
        handlers_chain=fake_chain
    )
    order = Order()

    app.run(order)

    assert fake_chain.handle_called_with(order) == True
    
def test_returns_valid_order_when_chain_returns_valid_order():
    fake_chain = FakeHandler().with_valid_order()
    app = make_sut(
        handlers_chain=fake_chain
    )
    order = Order()

    result = app.run(order)

    assert result.is_valid == True

def test_returns_invalid_order_when_chain_returns_invalid_order():
    fake_chain = FakeHandler()\
        .with_invalid_order(
            cause="Invalid order cause"
        )
    app = make_sut(
        handlers_chain=fake_chain
    )
    order = Order()

    result = app.run(order)

    assert result.is_valid == False
    assert result.cause == "Invalid order cause"

def test_throws_when_chain_returns_None():
    fake_chain = FakeHandler()\
        .with_None_result()
    app = make_sut(
        handlers_chain=fake_chain
    )
    order = Order()

    try:
        app.run(order)
        assert False
    except Exception as e:
        assert str(e) == "No handler could handle the order"

    

    