class Translation(object):
    START="<b>Hi {name}!</b> \n <code>I'm a simple bot transfer files between telegram & DMS that helps you to use data free downloads.</code> \n <b>Forward a file here to get started.</b>"
    DOWNLOADING="Downloading file to server..."
    DOWNLOADED="Downloaded successfully! Now uploading..."
    UPLOADING="Uploading file..."
    UPLOADED="Uploaded successfully to DMS!"
    HELP="Just forward a file to me, I'll do the rest!"
    ABOUT="Bot made by Kajatheepan. \n Source code: <a href='link'>GitHub</a>"


from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton

class InlineKeyboard(object):
    START=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ]]
    )

    HELP=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('About', callback_data='about')
        ]]
    )

    ABOUT=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data='start')
        ]]
    )
    