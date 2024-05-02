import threading
from time import sleep

import irc.client

from app.settings import TWITCH_ACCESS_TOKEN, TWITCH_CHANNEL, TWITCH_BOT_USERNAME


class TwitchChatBot:
    def __init__(self, nickname, password, channel, prefix='[AI bot]'):
        self.channel = channel
        self.prefix = prefix

        self.reactor = irc.client.Reactor()
        self.connection = self.reactor.server()
        self.connection.connect(
            'irc.chat.twitch.tv',
            6667,
            nickname=nickname,
            password=password,
        )
        while not self.connection.connected:
            print('Waiting for Twitch IRC chat connection...')
            sleep(1)

        print('Connected to Twitch IRC chat!')

    def message(self, message):
        self.connection.privmsg(self.channel, f'{self.prefix}: {message}')
        self.reactor.process_once()


ttv_chat = TwitchChatBot(
    nickname=TWITCH_BOT_USERNAME,
    password=TWITCH_ACCESS_TOKEN,
    channel=TWITCH_CHANNEL,
)
ttv_chat.message('test msg')
