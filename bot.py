from pyrogram import Client, filters
from pyrogram.errors import FloodWait

import time,os,json,sys
import asyncio

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
@app.on_message(filters.command("start"))
async def start(client,message):
    print('/start command recieved')
    await message.reply(
        text=Translation.START.format(name=message.from_user.first_name),
        reply_markup=InlineKeyboard.START,
    )

@app.on_message(filters.command("help"))
async def help(client, message):
    print('/help command recieved')
    await message.reply(
        text=Translation.HELP,
        reply_markup=InlineKeyboard.HELP,
    )
 
#MAIN function
async def main():
    async with app:
        print("Client started. Listening for messages...")
        try:
          await asyncio.Event().wait()  # Keeps the client running
        except KeyboardInterrupt:
            print("Client stopped due to keyboard interupt.")
        except:
          print("Client stopped.")


# Start the asyncio loop
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("An error occured.")
