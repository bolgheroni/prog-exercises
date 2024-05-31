class App:
    def __init__(self, handlers_chain):
        self.handlers_chain = handlers_chain

    def run(self, order):
        self.handlers_chain.handle(order)
        