class Transport:
    def __init__(self, type: str, capacity: int, speed_km_h: float, distance_km: float, id: int) -> None:
        self.type = type
        self.capacity = capacity
        self.speed_km_h = speed_km_h
        self.distance_km = distance_km
        self._is_deployed = False
        self.id = id
    
    def deploy(self):
        if  self.is_deployed():
            raise ValueError("This transport has already been deployed.")
        self._is_deployed = True
        print(f"Deploying {self.type} with capacity {self.capacity} to travel {self.distance_km} km at speed_km_h {self.speed_km_h} km/h.")

    def is_deployed(self):
        return self._is_deployed == True

    def get_eta(self):
        if not self.is_deployed():
            raise ValueError("This transport has not been deployed yet.")
        
        return self.distance_km / self.speed_km_h
        

    def __str__(self) -> str:
        if self.is_deployed():
            eta = self.get_eta()

            return f"{self.id}#{self.type} with capacity {self.capacity}, already deployed! ETA: {eta} hours."
        
        return f"{self.id}#{self.type} with capacity {self.capacity} not deployed yet."
