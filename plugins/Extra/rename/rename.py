from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random

@Client.on_message(filters.private & filters.command("rename"))
async def rename_start(client, message):
    msg = await client.ask(message.chat.id, "**Now send me your file/video/audio to rename.**")
    if not msg.media:
      return await message.reply("**Please send me supported media.**")
    if msg.media == (enums.MessageMediaType.VIDEO or enums.MessageMediaType.DOCUMENT or enums.MessageMediaType.AUDIO):
        file = getattr(msg, msg.media.value)
        filename = file.file_name
        filesize = humanize.naturalsize(file.file_size) 
        fileid = file.file_id
        try:
            text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                       [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
           # await sleep(FLOOD)
        except FloodWait as e:
            await sleep(e.value)
            text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                       [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        except:
            pass
      
