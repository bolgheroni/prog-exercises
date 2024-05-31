from src.models.handle_result import HandleResult
from src.handlers.handler import Handler
class App:
    def __init__(self, handlers_chain: Handler):
        self.handlers_chain = handlers_chain

    def run(self, order) -> HandleResult:
        result = self.handlers_chain.handle(order)
        if result is None:
            raise Exception("No handler could handle the order")
        
        return result

        
        