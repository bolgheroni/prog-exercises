from src.handlers.handlers_chain import HandlersChain
from src.handlers.cash_payment_handler import CashPaymentHandler
from src.handlers.inventory_handler import InventoryHandler
from src.handlers.validation_handler import ValidationHandler
from src.services.inventory import Inventory
from src.services.user_funds import UserFundsService

from src.models.order import Order
from src.models.order_item import OrderItem
from src.app import App

def main():
    user_funds_service = UserFundsService()
    user_funds_service.set_user_cash(user_id="John", funds=1000)
    inventory = Inventory(
        items=[
            {"product": "Banana", "quantity": 10},
        ]
    )
    chain = HandlersChain()\
        .add_handler(ValidationHandler())\
        .add_handler(InventoryHandler(
            inventory=inventory
        ))\
        .add_handler(CashPaymentHandler(
            user_funds_service=user_funds_service
        ))

    app = App(handlers_chain=chain)

    order = Order(
        items=[
            OrderItem(product="Banana", quantity=50, price=1.5),
        ],
        payment_method="cash",
        user_id="John"
    )

    result = app.run(order)

    if result.is_valid:
        print("Order is valid")
    else:
        print(f"Order is invalid: {result.cause}")


if __name__ == "__main__":
    main()
