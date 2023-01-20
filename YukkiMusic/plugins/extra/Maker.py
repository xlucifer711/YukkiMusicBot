import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["تنصيب","التنصيب"])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/54699e9f531dfac087926.jpg",
        caption=f"""• | سورس كرستين للتنصيب""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تنصيب الميوزك", url=f"https://t.me/iiqllll"),
                    InlineKeyboardButton(
                        "تنصيب التليثون ♡", url=f"https://t.me/c_r_source/7810"),
                ],
                [
                   InlineKeyboardButton(
                        "©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•® ", url=f"https://t.me/c_r_source"),
                ],       
            ]
        ),
    )