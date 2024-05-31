from src.handlers.cash_payment_handler import CashPaymentHandler
from src.models.order import Order
from tests.fake_handlers_chain import FakeHandlersChain
from src.handlers.handler import Handler
from src.services.user_funds import UserFundsService

def make_sut(
    next_handler: Handler = None,
    user_funds_service=None
):
    handler = CashPaymentHandler(
        user_funds_service=user_funds_service
    )

    handler.set_next(next_handler)

    return handler


def test_pass_handling_when_payment_method_is_not_cash():
    fake_chain = FakeHandlersChain()
    sut = make_sut(
        next_handler=fake_chain
    )
    order = Order(payment_method="credit_card")

    sut.handle(order)

    assert fake_chain.handle_called_with(order) == True


def test_returns_invalid_order_when_cash_isnt_enough():
    # Arrange
    user_funds_service = UserFundsService()
    user_funds_service.set_user_cash(user_id=1, funds=10)

    order = Order(
        payment_method="cash", 
        user_id=1, 
        items=[
            {"id": 1, "quantity": 2, "price": 20}
        ]
    )

    sut = make_sut(
        user_funds_service=user_funds_service
    )

    # Act
    result = sut.handle(order)

    # Assert
    assert result.is_valid == False
    assert result.cause == "Funds aren't enough"
