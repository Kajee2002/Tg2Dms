from pyrogram import Client, filters
from pyrogram.errors import FloodWait

import time,os,json,asyncio,sys

from configs import Configs
from translation import InlineKeyboard, Translation


#Initialise the bot
app = Client(
    "DMSBot",
    api_id=Configs.API_ID,
    api_hash=Configs.API_HASH,
    bot_token=Configs.BOT_TOKEN

)

#Start command
@app.on_message(filters.command(["start"]))
async def start(client,message):
    await message.reply_text(
        text=Translation.START.format(name=message.from_user.first_name),
        reply_markup=InlineKeyboard.START,
        parse_mode="html",
        quote=True
    )
