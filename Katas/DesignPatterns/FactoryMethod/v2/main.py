import sys
from src.stdin_input_collector import StdinInputCollector
from src.app_input_collector import AppInputCollector
from src.transport_factory import TransportFactory
from src.transports_control import TransportsControl
from src.app import App

def main():
    factory = TransportFactory(
        input_collector=StdinInputCollector(input_channel=input)
    )
    control = TransportsControl(
        transport_factory=factory
    )
    app = App(
        output_channel=sys.stdout,
        input_collector=AppInputCollector(input_channel=input),
        transports_control=control
    )
    
    while True:
        app.loop()

        if app.should_exit():
            return
        
    

if __name__ == "__main__":
    main()
