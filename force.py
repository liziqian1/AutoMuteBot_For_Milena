import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

MILENA_USER_ID = 5039198489
CHITANG_CHAT_ID = -1001193721792


async def ban_user():
    permissions = types.ChatPermissions(can_send_messages=False, can_send_media_messages=False)
    await bot.restrict_chat_member(chat_id=CHITANG_CHAT_ID, user_id=MILENA_USER_ID, permissions=permissions,
                                   until_date=datetime.datetime.now() + datetime.timedelta(minutes=10))

if __name__ == '__main__':
    #executor.start_polling(dp, skip_updates=False)
    ban_user()
