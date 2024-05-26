class StdinInputCollector():
    def __init__(self, input_channel):
        self.input_channel = input_channel
        
    def collect_distance(self):
        return int(self.input_channel("Enter the distance in km: "))        
    
    def collect_crew_amount(self):
        return int(self.input_channel("Enter the number of crew members: "))