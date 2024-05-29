from handlers.validation_handler import ValidationHandler
from handlers.inventory_handler import InventoryHandler
from models.order import Order

def get_order() -> Order:
    return Order()

def main():
    validation_chain = ValidationHandler().set_next(InventoryHandler(
        inventory=[
            {"name": "product1", "amount": 10},
            {"name": "product2", "amount": 20}
        ]
    ))
    order = Order(
        products=[
            {"name": "product1", "amount": 1},
            {"name": "product2", "amount": 2}
        ]
    )

    result = validation_chain.handle(order)

    if result.success:
        print("Order is valid")
    else:
        print("Order is invalid: ", result.message)


if __name__ == "__main__":
    main()
