from abc import ABC, abstractmethod


class Order():
    def __init__(self, products=None, buyer=None, delivery_address=None, payment_method=None, order_details=None):
        self.products = products
        self.buyer = buyer
        self.delivery_address = delivery_address
        self.payment_method = payment_method
        self.order_details = order_details


class HandleResult():
    def __init__(self, success=False, message=None):
        self.success = success
        self.message = message


class OrderHandler(ABC):
    @abstractmethod
    def handle(self, order: Order) -> HandleResult:
        pass


class BaseHandler(OrderHandler):
    def __init__(self):
        self.next = None

    def set_next(self, next_handler: OrderHandler) -> OrderHandler:
        self.next = next_handler
        return self

    def handle(self, order: Order) -> HandleResult:
        if self.next:
            return self.next.handle(order)
        else:
            return HandleResult(success=True)


class ValidationHandler(BaseHandler):
    def handle(self, order: Order) -> HandleResult:
        result = self.validate_products_length(order)
        if result:
            return result

        result = self.validate_products_amount(order)
        if result:
            return result

        return super().handle(order)

    def validate_products_length(self, order: Order) -> HandleResult | None:
        if not order.products:
            return HandleResult(success=False, message="No products in order")
        return None

    def validate_products_amount(self, order: Order) -> HandleResult | None:
        for product in order.products:
            if product["amount"] <= 0:
                return HandleResult(success=False, message="Product amount is invalid")
        return None


class InventoryHandler(BaseHandler):
    def __init__(self, inventory):
        super().__init__()
        self.inventory = inventory

    def handle(self, order: Order) -> HandleResult:
        result = self.check_inventory(order)
        if result:
            return result

        return super().handle(order)

    def check_inventory(self, order: Order) -> HandleResult | None:
        for product in order.products:
            if product["name"] not in [item["name"] for item in self.inventory]:
                return HandleResult(success=False, message=f"Product {product['name']} is not in inventory")
            
            inventory_product = next(item for item in self.inventory if item["name"] == product["name"])
            
            if inventory_product["amount"] <= 0:
                return HandleResult(success=False, message=f"Product {product['name']} is out of stock")
            
            if product["amount"] > inventory_product["amount"]:
                return HandleResult(success=False, message=f"Product {product['name']} stock amount is not sufficient")
            
        return None


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
