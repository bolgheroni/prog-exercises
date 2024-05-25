Context: Order Processing System

Scenario:
You are developing a system to handle customer orders. Orders can be placed online or in-store, each with different payment and delivery methods. The sequence of steps to process an order is the same, but the implementation of each step varies.

Objective:
Use the template pattern to define the order processing sequence while allowing customization for different order types.

Exercise:
Implement a template method for processing orders, with customizable steps for handling payment and delivery.

Desired Outcome:
- The order processing system should follow a consistent sequence of steps: order placement, payment processing, and delivery arrangement.
- For online orders:
  - Allow payment by debit or credit card.
  - Offer delivery options like home delivery or pick-up at a designated location.
- For in-store orders:
  - Allow payment by cash, debit, or credit card.
  - Offer immediate pick-up as the delivery option.
- Ensure each order type (online or in-store) can customize its payment and delivery steps within the overall processing sequence.