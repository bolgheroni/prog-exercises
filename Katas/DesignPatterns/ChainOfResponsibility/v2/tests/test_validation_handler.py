from src.models.order import Order
from src.handlers.validation_handler import ValidationHandler

def make_sut():
    return ValidationHandler()

def test_invalidates_empty_order():
    sut = make_sut()
    order = Order(
        items=[]
    )

    result = sut.handle(order)

    assert result.is_valid == False
    assert "empty" in result.cause.lower()
    