from v2.src.transport import Transport
from v2.src.transport_factory import TransportFactory

class TransportsControl:
    def __init__(self, transport_factory: TransportFactory):
        self.transports_list  = []
        self.transport_factory = transport_factory

    def create_transport(self, type: str, id: int) -> Transport:
        new_transport = self.transport_factory.create_transport(
            id=id,
            type=type
        )
        self.transports_list.append(new_transport)
        return new_transport
    
    def list_transports(self):
        return self.transports_list