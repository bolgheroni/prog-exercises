class HDMISignal:
    def __init__(self, sound_signal: str, video_signal: str):
        self.sound_signal = sound_signal
        self.video_signal = video_signal

    def __str__(self):
        return f"[HDMI: Sound signal: {self.sound_signal}, video signal: {self.video_signal}]"
    
class VGASignal:
    def __init__(self, video_signal: str):
        self.video_signal = video_signal

    def __str__(self):
        return f"[VGA: Video signal: {self.video_signal}]"

