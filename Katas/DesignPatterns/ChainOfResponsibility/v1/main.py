from handlers.validation_handler import ValidationHandler
from handlers.inventory_handler import InventoryHandler
from handlers.cash_payment_handler import CashPaymentHandler
from models.order import Order

def get_order() -> Order:
    return Order()

def main():
    validation_chain = ValidationHandler().set_next(InventoryHandler(
        inventory=[
            {"name": "product1", "amount": 10},
            {"name": "product2", "amount": 20}
        ]
    )).set_next(CashPaymentHandler())

    order = Order(
        products=[
            {"name": "product1", "amount": 1, "price": 10},
            {"name": "product2", "amount": 2, "price": 10},
        ],
        payment_method="cash",
        payment_details={"available_cash": 30},
    )

    result = validation_chain.handle(order)

    if result.success:
        print("Order is valid")
    else:
        print("Order is invalid: ", result.message)


if __name__ == "__main__":
    main()
