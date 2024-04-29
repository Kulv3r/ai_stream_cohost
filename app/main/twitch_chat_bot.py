import threading

import irc.client

from app.settings import TWITCH_ACCESS_TOKEN, TWITCH_CHANNEL, TWITCH_BOT_USERNAME


class TwitchChatBot:
    def __init__(self, nickname, password, channel):
        self.nickname = nickname
        self.password = password
        self.channel = channel
        self.reactor = irc.client.Reactor()

        self.connect()

    def connect(self):
        self.connection = self.reactor.server()
        try:
            self.connection.connect(
                'irc.chat.twitch.tv',
                6667,
                nickname=self.nickname,
                password=self.password,
            )
        except irc.client.ServerConnectionError as e:
            print(f'Failed to connect to IRC server: {e}')
            return

        # Start the IRC event loop in a separate thread
        self.thread = threading.Thread(target=self.reactor.process_forever)
        self.thread.start()

    def message(self, message):
        self.connection.privmsg(self.channel, f'[AI bot]: {message}')


ttv_chat = TwitchChatBot(
    nickname=TWITCH_BOT_USERNAME,
    channel=TWITCH_CHANNEL,
    password=TWITCH_ACCESS_TOKEN,
)
# ttv_chat.message('gg wp')
