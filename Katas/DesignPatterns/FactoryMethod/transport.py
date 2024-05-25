from abc import ABC

class Transport(ABC):
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

class TruckTransport(Transport):
    def __init__(self, distance_km: float, id: int) -> None:
        super().__init__("Truck", 50, 100, distance_km, id)

    def get_eta(self):
        base_eta = super().get_eta()
        # has to stop for refueling every 200 km
        refuel_stops = self.distance_km // 200
        return base_eta + refuel_stops * 0.5

class ShipTransport(Transport):
    def __init__(self, distance_km: float, id: int, crew_amount: int = 10) -> None:
        super().__init__("Ship", 500, 50 - crew_amount / 10, distance_km, id)

    def get_eta(self):
        base_eta = super().get_eta()
        # has to stop for refueling every 1000 km
        refuel_stops = self.distance_km // 1000
        return base_eta + refuel_stops * 4
