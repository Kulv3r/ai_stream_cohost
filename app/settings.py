import os

# Sound recording
SAMPLE_RATE = 44100  # Sample rate for the microphone
CHANNELS = 1  # Mono - Number of audio channels
DTYPE = 'float32'  # Data type of the recording
# MIC_NAME = 'Microphone (4- Tula Audio)'

# OpenAI API URLs
GPT4_URL           = 'https://api.openai.com/v1/chat/completions'
SPEECH_TO_TEXT_URL = 'https://api.openai.com/v1/audio/transcriptions'
TEXT_TO_SPEECH_URL = 'https://api.openai.com/v1/audio/speech'
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Twitch
TWITCH_BOT_USERNAME = 'ChatterPlug'
TWITCH_CHANNEL = 'kulv3r'
TWITCH_ID = os.environ['TWITCH_ID']
TWITCH_SECRET = os.environ['TWITCH_SECRET']
TWITCH_ACCESS_TOKEN = os.environ['TWITCH_ACCESS_TOKEN']
