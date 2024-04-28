import io
import os

from pydub import AudioSegment

from ai_co_streamer.app.settings import SAMPLE_RATE, CHANNELS


def convert_wav_to_mp3(audio_data):
    print('Converting to mp3...')
    audio_segment = AudioSegment.from_wav(
        audio_data.tobytes(),
        sample_width=audio_data.dtype.itemsize,
        frame_rate=SAMPLE_RATE,
        channels=CHANNELS,
    )
    # buffer = io.BytesIO()
    # # buffer.name = 'tmp.mp3'
    # buffer.name = os.getcwd() + '\\tmp.mp3'
    # print(buffer.name)
    # audio_segment.export(buffer, format='mp3', bitrate='192k')
    with open('test.mp3', 'wb') as f:
        audio_segment.export(f, format='mp3', bitrate='192k')

    # mp3 = buffer.getvalue()
    print('Converting complete.')
    # return mp3

# def convert_wav_to_mp3(audio_data):
#     print('Converting to mp3...')
#     audio_segment = AudioSegment(
#         data=audio_data.tobytes(),
#         sample_width=audio_data.dtype.itemsize,
#         frame_rate=SAMPLE_RATE,
#         channels=CHANNELS,
#     )
#     # buffer = io.BytesIO()
#     # # buffer.name = 'tmp.mp3'
#     # buffer.name = os.getcwd() + '\\tmp.mp3'
#     # print(buffer.name)
#     # audio_segment.export(buffer, format='mp3', bitrate='192k')
#     with open('test.mp3', 'wb') as f:
#         audio_segment.export(f, format='mp3', bitrate='192k')
#
#     # mp3 = buffer.getvalue()
#     print('Converting complete.')
#     # return mp3
