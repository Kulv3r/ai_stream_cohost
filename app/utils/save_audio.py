from io import BytesIO

import soundfile as sf

from app.settings import SAMPLE_RATE


def save_mp3_to_file(audio_mp3, filename='test_output.mp3'):
    with open(filename, 'wb') as f:
        f.write(audio_mp3)


def raw_to_wav(audio_data):
    wav_file = BytesIO()
    sf.write(wav_file, audio_data, SAMPLE_RATE, format='WAV')
    wav_file.seek(0)
    return wav_file
