class Order:
    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return not self.items