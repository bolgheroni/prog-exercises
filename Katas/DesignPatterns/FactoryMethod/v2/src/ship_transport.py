from v2.src.transport import Transport 

class ShipTransport(Transport):
    def __init__(self, type: str, id: int, crew_amount: int):
        super().__init__(type, id)
        self.crew_amount = crew_amount

    def __str__(self):
        base_description = super().__str__()
        crew_amount_text = f"Crew amount: {self.crew_amount}." 
        return f"{base_description}. {crew_amount_text}"