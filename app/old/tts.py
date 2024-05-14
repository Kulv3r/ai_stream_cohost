from app.integrations.openai import open_ai


def text_to_speech(text):
    print('Requesting text-to-speech...')
    response = open_ai.audio.speech.create(
        input=text,
        model='tts-1',
        voice='alloy',
        response_format='mp3',
    )

    audio_content = response.content
    print('Requesting text-to-speech complete.')
    return audio_content
