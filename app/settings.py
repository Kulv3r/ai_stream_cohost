from .secrets import *  # Do not "optimize".


# Constants
SAMPLE_RATE = 44100  # Sample rate for the microphone
CHANNELS = 1  # Mono - Number of audio channels
DTYPE = 'float32'  # Data type of the recording
# MIC_NAME = 'Microphone (4- Tula Audio)'

# OpenAI API URLs
GPT4_URL =           'https://api.openai.com/v1/chat/completions'
SPEECH_TO_TEXT_URL = 'https://api.openai.com/v1/audio/transcriptions'
TEXT_TO_SPEECH_URL = 'https://api.openai.com/v1/audio/speech'
