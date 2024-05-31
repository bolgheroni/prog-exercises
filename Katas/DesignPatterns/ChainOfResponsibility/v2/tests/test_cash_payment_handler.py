from src.handlers.cash_payment_handler import CashPaymentHandler
from src.models.order import Order
from src.models.order_item import OrderItem
from tests.fake_handlers_chain import FakeHandlersChain
from src.handlers.handler import Handler
from src.services.user_funds import UserFundsService

def make_sut(
    next_handler: Handler = None,
    user_funds_service=None
):
    _user_funds_service = user_funds_service if user_funds_service else UserFundsService()
    handler = CashPaymentHandler(
        user_funds_service=_user_funds_service
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
            OrderItem(
                price=20,
                product="product X",
                quantity=2
            )
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

def test_returns_valid_order_when_cash_is_enough():
    # Arrange
    user_funds_service = UserFundsService()
    user_funds_service.set_user_cash(user_id=1, funds=40)

    order = Order(
        payment_method="cash", 
        user_id=1, 
        items=[
            OrderItem(
                price=20,
                product="product X",
                quantity=2
            )
        ]
    )

    sut = make_sut(
        user_funds_service=user_funds_service
    )

    # Act
    result = sut.handle(order)

    # Assert
    assert result.is_valid == True
