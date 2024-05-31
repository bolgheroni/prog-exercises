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
        return self

    def handle(self, order) -> HandleResult:
        if len(self.handlers) == 0:
            return None
        return self.handlers[0].handle(order)

    def remove_handler_by_index(self, index: int):
        to_remove_handler = self.handlers[index]
        to_remove_next = None
        
        if index < len(self.handlers) - 1:
            to_remove_next = self.handlers[index + 1]
        if index > 0:
            self.handlers[index - 1].set_next(to_remove_next)

        self.handlers.remove(to_remove_handler)

    def remove_handler(self, handler: Handler):
        index = self.handlers.index(handler)
        self.remove_handler_by_index(index)