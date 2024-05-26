from src.stdin_input_collector import StdinInputCollector
from src.transport_factory import TransportFactory
from src.transports_control import TransportsControl

def main():
    factory = TransportFactory(
        input_collector=StdinInputCollector(input_channel=input)
    )
    control = TransportsControl(
        transport_factory=factory
    )
    control.create_transport(
        type="TRUCK",
        id=1
    )
    for transport in control.list_transports():
        print(transport)
    

if __name__ == "__main__":
    main()
