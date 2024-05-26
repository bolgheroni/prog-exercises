from src.transports_control import TransportsControl

class App():
    def __init__(self, output_channel, input_channel, transports_control: TransportsControl):
        self.output_channel = output_channel
        self.input_channel = input_channel
        self.transports_control = transports_control

    def loop(self):
        print(
            "1 - List transports\n2 - Create transport\n3 - Deploy transport\n4 - Exit",
            file=self.output_channel
        )
        action = self.input_channel.collect_action_input()

        if action == "1":
            print("Current Transports List", file=self.output_channel)
            transports = self.transports_control.list_transports()
            for transport in transports:
                print(transport, file=self.output_channel)
            return 
        
        if action == "2":
            type = self.input_channel.collect_create_type_input()
            id = self.input_channel.collect_id_input()
            self.transports_control.create_transport(
                type=type,
                id=id
            )