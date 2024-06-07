class ConstantRunner:
    def __init__(self, speed: int):
        self.speed = speed

    def act(self, runner):
        runner.state.position += self.speed
        