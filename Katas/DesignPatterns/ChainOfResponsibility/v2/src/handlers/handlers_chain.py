from src.handlers.handler import Handler
from src.models.handle_result import HandleResult

class HandlersChain(Handler):
    def __init__(self):
        self.handlers = []
        
    def add_handler(self, handler: Handler):
        self.handlers.append(handler)
        
    def handle(self, order) -> HandleResult:
        self.handlers[0].handle(order)