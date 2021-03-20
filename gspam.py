# Original By @danish_00
# Not for kids
# Don't Know Y I made this Lol



from userbot.utils import admin_cmd as danishehe
from userbot import bot as danish_00
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
@danish_00.on(danishehe(pattern="gspam"))
async def cobra(danish):
  try:
       await danish.client(ImportChatInviteRequest('TN49H8F_WJrFaH9T'))
  except UserAlreadyParticipantError:
        pass
  except:
        await danish.reply("[Join this group](https://t.me/joinchat/TN49H8F_WJrFaH9T)", link_preview=False)
        return
  async for msg in danish.client.iter_messages(-1001289633055):
   if msg:
    await danish.client.send_message(danish.chat_id, msg)