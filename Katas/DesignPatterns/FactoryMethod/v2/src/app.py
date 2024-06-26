from src.transports_control import TransportsControl

class App():
    def __init__(self, output_channel, input_collector, transports_control: TransportsControl):
        self._output_channel = output_channel
        self._input_collector = input_collector
        self._transports_control = transports_control
        self._should_exit = False

    def loop(self):
        print(
            "1 - List transports\n2 - Create transport\n3 - Deploy transport\n4 - Exit",
            file=self._output_channel
        )
        action = self._input_collector.collect_action_input()

        if action == 1:
            print("Current Transports List", file=self._output_channel)
            transports = self._transports_control.list_transports()
            for transport in transports:
                print(transport, file=self._output_channel)

            if len(transports) == 0:
                print("No transports available", file=self._output_channel)
            return
        
        if action == 2:
            type = self._input_collector.collect_create_type_input()
            id = self._input_collector.collect_id_input()
            self._transports_control.create_transport(
                type=type,
                id=id
            )
            return

        if action == 3:
            id = self._input_collector.collect_id_input()
            self._transports_control.deploy_transport(id=id)
            return

        print("Exiting...", file=self._output_channel)
        self._should_exit = True

    def should_exit(self):
        return self._should_exit