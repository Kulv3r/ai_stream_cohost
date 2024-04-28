from openai import OpenAI

from app.settings import OPENAI_API_KEY

open_ai = OpenAI(api_key=OPENAI_API_KEY)
