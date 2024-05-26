class Transport:
    def __init__(self, type: str, id: int, distance: int = None, crew_amount: int = None):
        self.type = type
        self.id = id
        self._is_deployed = False
        self.distance = distance
        self.crew_amount = crew_amount

    def deploy(self):
        self._is_deployed = True

    def is_deployed(self):
        return self._is_deployed
        
    
    def __str__(self):
        distance_text = f"Distance: {self.distance}." if self.distance else ""
        crew_amount_text = f"Crew amount: {self.crew_amount}." if self.crew_amount else ""
        return f"{self.type} - {self.id}. {distance_text} {crew_amount_text}"