from src.models.handle_result import HandleResult

class App:
    def __init__(self, handlers_chain):
        self.handlers_chain = handlers_chain

    def run(self, order) -> HandleResult:
        return self.handlers_chain.handle(order)

        
        