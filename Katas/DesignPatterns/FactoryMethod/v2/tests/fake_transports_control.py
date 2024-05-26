from typing import List
from src.transport import Transport

class FakeTransportsControl:
    def __init__(self):
        self.transports_list: List[Transport] = []
        self.create_calls = []
        self.deploy_calls = []

    def set_transports_list(self, transports_list: List[Transport]):
        self.transports_list = transports_list
        return self
    
    def list_transports(self)-> List[Transport]:
        return self.transports_list
    
    def create_transport(self, type, id):
        self.create_calls.append({
            "type": str(type),
            "id": str(id)
        })

    def deploy_transport(self, id):
        self.deploy_calls.append({
            "id": str(id)
        })

    def called_create_transport(self, type, id):
        print(self.create_calls)
        return {
            "type": str(type),
            "id": str(id)
        } in self.create_calls
    
    def called_deploy_transport(self, id):
        return {
            "id": str(id)
        } in self.deploy_calls