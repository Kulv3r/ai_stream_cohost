from io import BytesIO

import sounddevice as sd
import soundfile as sf

from app.settings import SAMPLE_RATE, CHANNELS


def record_audio(
        duration=2,  # sec
):
    """
    Record audio from default mic.

    :param duration: record length, in seconds
    :return: ndarray of recordd bytes
    """
    print('RECORDING!')
    print('RECORDING!')
    print('RECORDING!')
    # sd.default.device = 3
    dur_frames = int(duration * SAMPLE_RATE)
    recording = sd.rec(
        dur_frames,
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        blocking=True,
    )
    print('Recording complete.')
    return recording


def play_recording(recording):
    # sd.default.device = 7
    sd.play(
        recording,
        samplerate=SAMPLE_RATE,
        blocking=True,
    )
