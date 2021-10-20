# Ported By @VckyouuBitch From Geez - Projects
# Copyright © Team Geez - Project

from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest

from userbot.events import register
from userbot import CMD_HELP


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.malingorang(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        geez = await event.reply("`proses sabar...`")
    else:
        geez = await event.edit("`proses sabar...`")
    geezteam = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await geez.edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = 'None'

    await geez.edit("**Status Sedang mencari mangsa**\n\n`menculik`")
    async for user in event.client.iter_participants(geezteam.full_chat.id):
        try:
            if error.startswith("Too"):
                return await geez.edit(f"**Menculik selesai With Error**\n(`Dapat peringatan dari orangtuanya`)\n**Error** : \n`{error}`\n\n• TerMaling `{s}` Orang \n• GagalMaling `{f}` orang")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await geez.edit(f"**Processing Penculikan...**\n\n• Maling `{s}` Orang \n• GagalMaling `{f}` orang\n\n**× Penculikan Error:** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await geez.edit(f"**Terminal Finished** \n\n• Sukses Maling `{s}` Orang \n• GagalMaling `{f}` Orang")


CMD_HELP.update({
    "malingorang":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.malingorang groups username`\
          \n📌 : __Scrapes users from the given chat to your group__."
})
