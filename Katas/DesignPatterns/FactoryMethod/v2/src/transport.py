class Transport:
    def __init__(self, type: str, id: int, distance: int = 0):
        self.type = type
        self.id = id
        self._is_deployed = False
        self.distance = distance

    def deploy(self):
        self._is_deployed = True

    def is_deployed(self):
        return self._is_deployed
        
    
    def __str__(self):
        return f"{self.type} - {self.id}. Distance: {self.distance}"