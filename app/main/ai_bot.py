from app.main import ai_prompts
from app.main.gpt import ask_gpt
from app.main.stt import speech_to_text
from app.main.twitch_chat_bot import ttv_chat
from app.main.unlim_rec import record
from app.utils.save_audio import raw_to_wav


class AIBot:
    def __init__(self):
        self.discussion = [
            {'role': 'system', 'content': ai_prompts.setup},
            # {'role': 'assistant', 'content': '???'},
            # {'role': 'user', 'content': '???'},
        ]

    def run(self):
        # Start recording, stop on SPACE key press
        raw_audio_as_nparray = record()
        wav_file = raw_to_wav(raw_audio_as_nparray)

        # Transcribe sound to text
        my_text_req = speech_to_text(wav_file)
        if not my_text_req:
            return
        self.discussion.append({'role': 'user', 'content': my_text_req})

        # Ask GPT, get response
        ai_text_resp = ask_gpt(self.discussion)
        if not ai_text_resp:
            return
        self.discussion.append({'role': 'assistant', 'content': ai_text_resp})

        # Write GPT response to chat
        ttv_chat.message(ai_text_resp)
