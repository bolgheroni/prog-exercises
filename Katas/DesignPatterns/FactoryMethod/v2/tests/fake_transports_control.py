from typing import List
from src.transport import Transport

class FakeTransportsControl:
    def __init__(self):
        self.transports_list: List[Transport] = []

    def set_transports_list(self, transports_list: List[Transport]):
        self.transports_list = transports_list
        return self
    
    def list_transports(self)-> List[Transport]:
        return self.transports_list