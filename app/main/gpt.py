from ai_co_streamer.app.integrations.openai import open_ai


def ask_gpt(text):
    print('Asking GPT...')
    response = open_ai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system',
             'content': 'You are Muhammad Ali, in a grumpy mood. Your answers can be sarcastic, a bit angry or toxic.'},
            {'role': 'user', 'content': text},
        ]
    )
    answer = response.choices[0].message.content
    print(f'GPT answered: "{answer}"')
    return answer
