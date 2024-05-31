from src.models.order import Order
from src.models.order_item import OrderItem
from src.handlers.inventory_handler import InventoryHandler
from src.services.inventory import Inventory

def make_sut(
    inventory: Inventory | None = None
):
    _inventory = inventory if inventory else Inventory()
    return InventoryHandler(
        inventory=_inventory
    )

def test_invalidates_unavailable_items():
    inventory = Inventory(
        items=[
            {
                "product": "Product 1",
                "quantity": 0
            },
            {
                "product": "Product 2",
                "quantity": 10
            }
        ]
    )
    sut = make_sut(
        inventory=inventory
    )
    order = Order(
        items=[
            OrderItem(
                product="Product 2",
                quantity=10,
            ),
            OrderItem(
                product="Product 1",
                quantity=22,
            ),
        ]
    )

    result = sut.handle(order)

    assert result.is_valid == False, "Expected the order to be invalid"
    assert "unavailable" in result.cause.lower(), "Expected the unavailable label to be in the cause message"
    assert "22" in result.cause.lower(), "Expected the quantity value to be in the cause message"
    assert "product 1" in result.cause.lower(), "Expected the product name to be in the cause message"

def test_validates_available_items():
    inventory = Inventory(
        items=[
            {
                "product": "Product 1",
                "quantity": 22
            }
        ]
    )
    sut = make_sut(
        inventory=inventory
    )
    order = Order(
        items=[
            OrderItem(
                product="Product 1",
                quantity=22,
            )
        ]
    )

    result = sut.handle(order)

    assert result.is_valid == True, "Expected the order to be valid"