from openai import BadRequestError

from app.integrations.openai import open_ai


def speech_to_text(audio_file):
    print('Requesting speech-to-text...')
    # audio_mp3 = io.BytesIO(audio_mp3)
    # audio_mp3.name = 'tmp.mp3'
    try:
        transcription = open_ai.audio.transcriptions.create(
            model='whisper-1',
            file=('file.wav', audio_file),
            language='en',
            temperature=0,
        )
    except BadRequestError:
        with open('test_output.wav', 'wb') as f:
            f.write(audio_file.getvalue())

        raise

    text = transcription.text
    print(f'Resulted text: "{text}"')
    return text
