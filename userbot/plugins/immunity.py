from datetime import datetime

from .. import ALIVE_NAME
from ..utils import admin_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "B Lac User"


@borg.on(admin_cmd(pattern="chod$"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "__**(❛ Dunga ❜!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**Ajaao Bhosdiwalo Chud Ne Ke Liye!!*_Mere Master Ki Immunity -->\n\n   ⚘ {ms}\n   ⚘ __**Mere Master Ke Pass Abhi Immunity Hai Ajao Kissi Ko Chud Ke Dikhenge **__ __** Pyare Immunity Wale Master**__ [{DEFAULTUSER}]"
    )
