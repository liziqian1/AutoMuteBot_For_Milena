import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

MILENA_USER_ID = 5039198489
CHITANG_CHAT_ID = -1001193721792

WORDS = {
    1.0:
        ['menshit', '痢癞客'],
    0.7:
        ['微软员工', 'menci', '鼠辈', '去他妈', '用户中心', '中心用户'],
    0.5:
        ['依云', 'felix', 'farsee', 'archcn', 'arch cn'],  # 针对archcn的往事
    0.3:
        ['arch linux', 'archlinux', '晦气']
}


async def ban_user(message: types.Message):
    await message.reply('先去冷静冷静... qwq')
    permissions = types.ChatPermissions(can_send_messages=False, can_send_media_messages=False)
    # await bot.restrict_chat_member(chat_id=MILENA_USER_ID, user_id=message.from_user.id, permissions=permissions,ntil_date=datetime.datetime.now() + datetime.timedelta(minutes=10))


def special_filter(lower_message: str):
    add_weight: float = 0.0
    if 'arch' in lower_message:
        add_weight = 0.3
        if 'sb ' in lower_message or '鸡巴' in lower_message or '垃圾' in lower_message:
            add_weight = 1.0  # 开始发病了
        if '为什么' in lower_message:
            add_weight = 0.9  # 为什么arch有xxx：发病前兆
    return add_weight


@dp.message_handler()
async def message_handler(message: types.Message):
    weight: float = 0.0
    lower_message = message.text.lower()
    for add_weight in WORDS:
        for word in WORDS[add_weight]:
            if word in lower_message:
                weight += add_weight
    weight += special_filter(lower_message)
    if weight >= 1.0:
        await ban_user(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
