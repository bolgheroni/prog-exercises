Context: Logistics Management Application

Scenario:
You are creating a logistics management application initially focused on truck transportation. As your app gains popularity, you receive requests to include sea transportation (e.g., ships).

Objective:
You need to extend the application to handle different types of transportation without tightly coupling the code to specific transportation methods.

Exercise:
Implement a factory method to create transportation objects based on the type of transportation required.

Desired Outcome:
- The application can dynamically instantiate different types of transportation (e.g., trucks, ships).
- Users can specify the type of transportation needed (e.g., "truck" or "ship") when creating a transport instance.
- The system can easily incorporate new transportation types (e.g., air transport) without changing the existing code.