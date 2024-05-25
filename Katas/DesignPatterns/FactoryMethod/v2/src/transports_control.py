from v2.src.transport import Transport

class TransportsControl:
    def __init__(self):
        self.transports_list  = []

    def create_transport(self, type: str, id: int) -> Transport:
        new_transport = Transport(
            type=type,
            id=id
        )
        self.transports_list.append(new_transport)
        return new_transport
    
    def list_transports(self):
        return self.transports_list