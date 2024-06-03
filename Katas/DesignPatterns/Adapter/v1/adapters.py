from cables import Cable
from sources import VGASource, HDMISource
from signals import VGASignal, HDMISignal

class HDMIToVGAAdapter(Cable):
    def __init__(self):
        self.source = None

    def connect(self, source: HDMISource):
        print("HDMI to VGA adapter connected!")
        self.source = source

    def get_signal(self) -> VGASignal:
        _hdmi_signal = self.source.get_signal()
        return VGASignal(video_signal=_hdmi_signal.video_signal)

class VGAToHDMIAdapter(Cable):
    def __init__(self):
        self.source = None

    def connect(self, source: VGASource):
        print("VGA to HDMI adapter connected!")
        self.source = source

    def get_signal(self) -> HDMISignal:
        _vga_signal = self.source.get_signal()
        return HDMISignal(sound_signal='', video_signal=_vga_signal.video_signal)