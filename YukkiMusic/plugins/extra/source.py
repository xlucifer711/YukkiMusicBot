import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USER = getenv("BOT_USER")

@app.on_message(
    command(["سورس مين","سورس","السورس","يا سورس","سورس كرستين"])
    & ~filters.edited
)
async def taiger(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9fd0a28073d92e3052fe3.jpg",
        caption=f"""╭──★──[ᥴ.ᖇ ᥉᥆υᖇᥴᥱ](https://t.me/c_r_source)──★──╮\n么 [ᥴ.ᖇ ᥉᥆υᖇᥴᥱ](https://t.me/c_r_source)  \n么 [Dev zeιn](http://t.me/iiqllll) \n么 [dev crιѕтιn](http://t.me/dr_criss) \n么 [dev вarlo](http://t.me/bar_lo0o0)\n╰──★──[ᥴ.ᖇ ᥉᥆υᖇᥴᥱ](https://t.me/c_r_source)──★──╯ \n[ᥴ.ᖇ ᥉᥆υᖇᥴᥱ](https://t.me/c_r_source)""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton(
                        "ᥴ.ᖇ ᥉᥆υᖇᥴᥱ", url=f"https://t.me/c_r_source")
                 ],   
                 [    
                    InlineKeyboardButton(
                        "اضف البوت ف جروبك ✨️", url=f"https://t.me/{BOT_USER}?startgroup=true")
                 ],
             ]
            ),
    )
  
