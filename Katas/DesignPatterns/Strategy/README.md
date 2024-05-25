# Context: 
Sports Event Simulator
# Scenario:
You are developing a sports event simulator that initially supports marathon and 10 km run events, where competitors can be displayed and compete by running. You later add marshals and triathlon events, where competitors compete by swimming, cycling, and running.

# Objective:
Use the strategy pattern to define different competition strategies for various sports events, allowing easy extension of the system without modifying existing code.

# Exercise:
Implement different strategies for competitors to participate in various sports events.

# Desired Outcome:
- The simulator should support multiple event types (marathon, 10 km run, triathlon).
- For each event:
  - Competitors can be displayed and can compete in the event.
- Marshals can be displayed but do not compete in events.
- Ensure the system can easily incorporate new event types and competition strategies without modifying existing code.