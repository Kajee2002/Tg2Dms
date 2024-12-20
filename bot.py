from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

@app.on_message(filters.command("start"))
async def start(client,message):
  inline_keyboard3 = InlineKeyboardMarkup([
      [InlineKeyboardButton('Bulk Upload', callback_data='bulkupload'), InlineKeyboardButton('DMS details', callback_data='dms')],
      [InlineKeyboardButton('Cancel', callback_data='cancel')]
  ])
  await message.reply_text(f"Hello {message.from_user.first_name}!\n I'm able to move your telegram files to DMS UoM.",reply_to_message_id=message.id,reply_markup=inline_keyboard3)

@app.on_message(filters.document)
async def download(client, message):
    print('Document recieved')
    await message.reply(Translation.DOWNLOADING)
 
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
