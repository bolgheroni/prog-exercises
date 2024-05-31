from src.app import App
from tests.fake_handlers_chain import FakeHandlersChain
from src.models.order import Order

def make_sut(
    handlers_chain
):
    app = App(
        handlers_chain=handlers_chain
    )
    return app

def test_pass_order_to_handlers_chain():
    fake_chain = FakeHandlersChain()
    app = make_sut(
        handlers_chain=fake_chain
    )
    order = Order()

    app.run(order)

    assert fake_chain.handle_called_with(order) == True
    
def test_returns_valid_order_when_chain_returns_valid_order():
    fake_chain = FakeHandlersChain().with_valid_order()
    app = make_sut(
        handlers_chain=fake_chain
    )
    order = Order()

    result = app.run(order)

    assert result.is_valid == True

def test_returns_invalid_order_when_chain_returns_invalid_order():
    fake_chain = FakeHandlersChain()\
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