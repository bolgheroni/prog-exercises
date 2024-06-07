class Marathon:
    def __init__(self):
        self.participants = []

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self):
        return '\n'.join([f'{name} {age}' for name, age in self.participants])