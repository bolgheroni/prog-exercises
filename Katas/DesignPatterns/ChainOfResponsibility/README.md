# Context: 
Order Processing Workflow

# Scenario:
In an order processing workflow, an order goes through various stages: validation, inventory check, payment verification, and shipping confirmation. Each stage is handled by a different component.

# Objective:
Use the chain of responsibility pattern to manage the order processing stages, allowing each handler to process or pass the request along the chain.

# Exercise:
Implement a chain of responsibility to process orders through various stages.

# Desired Outcome:
- The system should route each order through a sequence of handlers: validation, inventory check, payment verification, and shipping confirmation.
- Each handler processes its specific aspect of the order:
  - Validation ensures the order details are correct.
  - Inventory checks stock availability.
  - Payment verifies payment information.
  - Shipping confirms shipping details.
- If a handler cannot process an order, it passes the order to the next handler in the chain.
- Ensure the order processing workflow is modular and can be easily extended with new handlers if needed.