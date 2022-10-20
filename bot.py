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
        ['menshit', '痢癞客', 'arshit'],
    0.7:
        ['微软员工', 'menci', '鼠辈', '去他妈', '用户中心', '中心用户', '傻逼', 'sb ', 'sb的', '智商','dick','dich'],
    0.5:
        ['依云', 'felix', 'farsee', 'archcn', 'arch cn'],  # 针对archcn的往事
    0.3:
        ['arch linux', 'archlinux', '晦气', 'pacman', '包管理器', 'nix']
}


async def ban_user(message: types.Message):
    await message.reply(
        '你说的对，但是我认为 ' + message.text + ' 应该在 IPhone 14 Pro Max 非海南免税版上运行 MSDOS 然后执行 sudo pacman -Syu ，然后他就可以把 NixOS 升级到最新版本，这就意味着一个风滚草用户开始了桶滚，不过 AMD 显卡的用户要注意，Windows Update 可能会搞坏你在 Android 上的 Nvidia 显卡驱动，所以更新 Windows 10 Mobile 可以给 iPhone 3gs 用户带来更佳的 Gentoo 使用体验，综上所述，用 波音787 搞渗透是可行的，但是前提是你能够熟练的开火车，这样才能用胶带开启虫洞进行星际穿越。')
    permissions = types.ChatPermissions(can_send_messages=False, can_send_media_messages=False)
    await bot.restrict_chat_member(chat_id=CHITANG_CHAT_ID, user_id=MILENA_USER_ID, permissions=permissions,
                                   until_date=datetime.datetime.now() + datetime.timedelta(minutes=10))


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
    if message.from_user.id != MILENA_USER_ID:
        return
    weight: float = 0.0
    lower_message = message.text.lower()
    for add_weight in WORDS:
        for word in WORDS[add_weight]:
            if word in lower_message:
                weight += add_weight
    weight += special_filter(lower_message)
    print(f'{lower_message} {weight}')
    if weight >= 1.0:
        print(lower_message)
        await ban_user(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
