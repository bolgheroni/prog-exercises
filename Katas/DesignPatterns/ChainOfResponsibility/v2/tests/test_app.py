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
    