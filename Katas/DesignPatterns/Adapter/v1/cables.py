from abc import ABC, abstractmethod
from sources import VGASource, HDMISource
from signals import VGASignal, HDMISignal

class Cable(ABC):
    @abstractmethod
    def connect(self, source):
        pass

    @abstractmethod
    def get_signal(self):
        pass

class VGACable(Cable):
    def __init__(self):
        self.source = None

    def connect(self, source: VGASource):
        print("VGA connected")
        self.source = source

    def get_signal(self) -> VGASignal:
        return self.source.get_signal()

class HDMICable(Cable):
    def __init__(self):
        self.source = None

    def connect(self, source: HDMISource):
        print("HDMI connected")
        self.source = source

    def get_signal(self) -> HDMISignal:
        return self.source.get_signal()