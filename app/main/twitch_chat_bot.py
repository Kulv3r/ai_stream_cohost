import threading
from time import sleep

import irc.client

from app.settings import TWITCH_ACCESS_TOKEN, TWITCH_CHANNEL, TWITCH_BOT_USERNAME


class TwitchChatBot:
    def __init__(self, nickname, password, channel, prefix='[AI bot]'):
        self.nickname = nickname
        self.password = password
        self.channel = channel
        self.prefix = prefix

        self.reactor = irc.client.Reactor()
        self.connection = self.reactor.server()
        self.connect()

    def connect(self):
        if self.connection.connected:
            return

        self.connection.connect(
            'irc.chat.twitch.tv',
            6667,
            nickname=self.nickname,
            password=self.password,
        )
        while not self.connection.connected:
            print('Waiting for Twitch IRC chat connection...')
            sleep(1)

        print('Connected to Twitch IRC chat!')

    def message(self, message):
        # Reconnect if needed
        self.connect()

        for message_part in message.split('\n'):
            if message_part.strip():
                try:
                    self.connection.privmsg(self.channel, f'{self.prefix}: {message_part}')
                except irc.client.MessageTooLong:
                    # If message is too long (> 512b), split in 2 and retry recursively
                    msg1 = message_part[:len(message_part)//2]
                    msg2 = message_part[len(msg1):]
                    self.message(msg1)
                    self.message(msg2)

        self.reactor.process_once()


ttv_chat = TwitchChatBot(
    nickname=TWITCH_BOT_USERNAME,
    password=TWITCH_ACCESS_TOKEN,
    channel=TWITCH_CHANNEL,
)
