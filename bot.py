import os

from aiogram.types import Message
from bestconfig import Config

from aiogram import Bot, Dispatcher

config = Config()

bot = Bot(token=config.API_TOKEN)

dp = Dispatcher(bot)


users = set()


def read_users():
    global users
    if os.path.exists('ids.txt'):
        with open('ids.txt', 'r') as f:
            for user in f.read().split():
                if user.strip():
                    users.add(int(user))


@dp.message_handler(commands=['start'])
async def start(message: Message):
    with open('ids.txt', 'a') as f:
        f.write(str(message.from_user.id) + '\n')

    users.add(message.from_user.id)
    await message.answer('Added')


async def send_text_broadcast(text):
    for user in users:
        await bot.send_message(user, text)
