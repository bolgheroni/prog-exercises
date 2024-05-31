from src.handlers.handler import Handler
from src.models.handle_result import HandleResult
from abc import abstractmethod

class BaseHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def handle(self, order) -> HandleResult | None:
        if not self._can_handle(order):
            return self._next_handler_result(order)
            
        current_handle_result = self._handle_specific(order)

        if not current_handle_result.is_valid:
            return current_handle_result
        
        next_handler_result = self._next_handler_result(order)

        if next_handler_result:
            return next_handler_result
        
        return current_handle_result 

    def set_next(self, next_handler: Handler):
        self.next_handler = next_handler

    def _next_handler_result(self, order) -> HandleResult | None:
        if self.next_handler:
            return self.next_handler.handle(order)
        return None
    
    @abstractmethod
    def _can_handle(self, order) -> bool:
        pass

    @abstractmethod
    def _handle_specific(self, order) -> HandleResult:
        pass