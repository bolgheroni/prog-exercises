from v2.src.transport import Transport

class TransportFactory:
    def __init__(self, input_collector):
        self.input_collector = input_collector

    def create_transport(self, id: int, type: str):
        distance = self.input_collector.collect_distance() if type == "TRUCK" else None
        crew_amount = self.input_collector.collect_crew_amount() if type == "SHIP" else None
        return Transport(
            type=type,
            id=id,
            distance=distance,
            crew_amount=crew_amount
        )