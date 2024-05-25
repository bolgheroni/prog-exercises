from v2.src.transport import Transport

class TransportFactory:
    def create_transport(self, id: int, type: str):
        return Transport(
            type=type,
            id=id
        )