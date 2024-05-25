class Transport:
    def __init__(self, type: str, capacity: int, speed_km_h: float, distance_km: float, id: int) -> None:
        self.type = type
        self.capacity = capacity
        self.speed_km_h = speed_km_h
        self.distance_km = distance_km
        self.deployment_time_hour = None
        self.id = id
    
    def deploy(self, current_hour: int):
        if self.deployment_time_hour != None:
            raise ValueError("This transport has already been deployed.")
        self.deployment_time_hour = current_hour
        print(f"Deploying {self.type} with capacity {self.capacity} to travel {self.distance_km} km at speed_km_h {self.speed_km_h} km/h. Deployment time: {self.deployment_time_hour} hours.")

    def is_deployed(self):
        return self.deployment_time_hour != None

    def get_eta(self, current_time):
        if not self.is_deployed():
            raise ValueError("This transport has not been deployed yet.")
        
        total_time = self.distance_km / self.speed_km_h
        return total_time - current_time

    def __str__(self) -> str:
        if self.is_deployed():
            eta = self.get_eta()
            if eta < 0:
                return f"{self.id}#{self.type} with capacity {self.capacity} deployed at {self.deployment_time_hour} hours. Already arrived."
            
            return f"{self.id}#{self.type} with capacity {self.capacity} deployed at {self.deployment_time_hour} hours. ETA: {eta} hours."
        
        return f"{self.id}#{self.type} with capacity {self.capacity} not deployed yet."
