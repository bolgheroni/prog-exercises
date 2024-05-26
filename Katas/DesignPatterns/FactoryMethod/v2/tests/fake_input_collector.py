class FakeInputCollector:
    def __init__(self):
        self.distance = 100
    def set_distance(self, distance):
        self.distance = distance
        return self

    def collect_distance(self):
        return self.distance
    
