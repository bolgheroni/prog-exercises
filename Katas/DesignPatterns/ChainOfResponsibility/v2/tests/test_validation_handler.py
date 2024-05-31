from src.models.order import Order
from src.models.order_item import OrderItem
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
    
def test_validates_order_with_items():
    sut = make_sut()
    order = Order(
        items=[
            OrderItem(
                product="Product 1",
                quantity=1,
            )
        ]
    )

    result = sut.handle(order)

    assert result.is_valid == True

def test_invalidates_order_with_invalid_item_quantities():
    sut = make_sut()
    order1 = Order(
        items=[
            OrderItem(
                product="Product 1",
                quantity=0,
            )
        ]
    )
    order2 = Order(
        items=[
            OrderItem(
                product="Product 1",
                quantity=-1,
            )
        ]
    )

    result1 = sut.handle(order1)
    result2 = sut.handle(order2)

    assert result1.is_valid == False, "Expected order 1 to be invalid"
    assert "quantity" in result1.cause.lower(), "Expected the quantity label to be in the cause message"
    assert "0" in result1.cause, "Expected the quantity value to be in the cause message"
    assert "Product 1" in result1.cause, "Expected the product name to be in the cause message"

    assert result2.is_valid == False, "Expected order 2 to be invalid"
    assert "quantity" in result2.cause.lower(), "Expected the quantity label to be in the cause message"
    assert "-1" in result2.cause, "Expected the quantity value to be in the cause message"
    assert "Product 1" in result2.cause, "Expected the product name to be in the cause message"
    