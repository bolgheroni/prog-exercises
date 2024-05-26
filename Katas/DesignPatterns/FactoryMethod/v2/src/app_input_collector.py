class AppInputCollector():
    def __init__(self, input_channel):
        self.input_channel = input_channel
        
    def collect_action_input(self):
        return int(self.input_channel("Enter the action: "))
    
    def collect_create_type_input(self):
        return self.input_channel("Enter the Transport type: ")
    
    def collect_id_input(self):
        return int(self.input_channel("Enter the Transport id: "))
    