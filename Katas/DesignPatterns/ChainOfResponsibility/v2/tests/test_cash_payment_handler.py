from src.handlers.cash_payment_handler import CashPaymentHandler
from src.models.order import Order
from tests.fake_handlers_chain import FakeHandlersChain
from src.handlers.handler import Handler


def make_sut(
    next_handler: Handler
):
    return CashPaymentHandler().set_next(next_handler)


def test_pass_handling_when_payment_method_is_not_cash():
    fake_chain = FakeHandlersChain()
    sut = make_sut(
        next_handler=fake_chain
    )
    order = Order(payment_method="credit_card")

    sut.handle(order)

    assert fake_chain.handle_called_with(order) == True
