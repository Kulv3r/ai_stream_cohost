from app.main.ai_bot import AIBot


def main():
    ai_bot = AIBot()
    while True:
        ai_bot.run()
        input('Press [ENTER] to continue...')


if __name__ == '__main__':
    main()
