from app.integrations.openai import open_ai


def ask_gpt(messages):
    print('Asking GPT...')
    response = open_ai.chat.completions.create(
        model='gpt-4',
        messages=messages,
        # messages=[
        #     {'role': 'system',
        #      'content': 'You are... Your answers can be...'},
        #     {'role': 'user', 'content': text},
        # ]
    )
    answer = response.choices[0].message.content
    print(f'GPT answered: "{answer}"')
    return answer
