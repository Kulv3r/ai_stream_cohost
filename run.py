from ai_co_streamer.app.old.play_mp3 import play_audio
from app.main.stt import speech_to_text
from app.utils.save_audio import save_mp3_to_file, raw_to_wav
from ai_co_streamer.app.old.record import record_audio


def main():
    audio_data = record_audio()
    wav_file = raw_to_wav(audio_data)
    text = speech_to_text(wav_file)

    return
    if text:
        response_text = ask_gpt(text)
        response_audio = text_to_speech(response_text)
        save_mp3_to_file(response_audio, 'test_output.mp3')
        play_audio(response_audio)
    else:
        print('No speech detected, trying again...')


def mmmmain():
    '''
    start recording
    stop on key press
    transcribe, ask gpt, get response, write to chat
    keep dialogue text
    repeat

    :return:
    '''


if __name__ == '__main__':
    # while True:
    main()
