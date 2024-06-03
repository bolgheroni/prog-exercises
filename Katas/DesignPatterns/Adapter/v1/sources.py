import random
import string
from signals import VGASignal, HDMISignal

class VGASource:
    def get_signal(self) -> VGASignal:
        _random_signal = random_string(10)
        return VGASignal(video_signal=_random_signal)

class HDMISource:
    def get_signal(self) -> HDMISignal:
        _random_sound_signal = random_string(10)
        _random_video_signal = random_string(10)
        return HDMISignal(sound_signal=_random_sound_signal, video_signal=_random_video_signal)
    
def random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
