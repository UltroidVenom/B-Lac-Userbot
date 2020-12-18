#created by @cyper666
"""xoxbot: Avaible commands: .sxy <link>
"""


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="sxy?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@sexgir_bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=183226019))
              await event.client.send_message(chat, "⭕️⭕️⭕️ {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Unblock @sexgir_bot```")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("😐")
          else: 
             await event.delete()
             await event.client.send_file(event.chat_id, response.message)
