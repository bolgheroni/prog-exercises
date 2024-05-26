class FakeInputCollector:
    def __init__(self):
        self.distance = 100
    def set_distance(self, distance):
        self.distance = distance
        return self

    def set_crew_amount(self, crew_amount):
        self.crew_amount = crew_amount
        return self

    def set_action_input(self, action_input):
        self.action_input = action_input
        return self
    
    def collect_distance(self):
        return self.distance
    
    def collect_crew_amount(self):
        return self.crew_amount

    def collect_action_input(self):
        return self.action_input