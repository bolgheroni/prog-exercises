from src.handlers.handler import Handler
from src.models.handle_result import HandleResult

class HandlersChain(Handler):
    def __init__(self):
        self.handlers = []
        
    def add_handler(self, handler: Handler):
        last_handler = self.handlers[-1] if len(self.handlers) > 0 else None
        if last_handler:
            last_handler.set_next(handler)
        self.handlers.append(handler)

    def handle(self, order) -> HandleResult:
        if len(self.handlers) == 0:
            return None
        self.handlers[0].handle(order)