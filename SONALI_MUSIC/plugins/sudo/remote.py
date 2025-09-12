# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from SONALI_MUSIC import app
from datetime import datetime
import os
from config import OWNER_ID
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
import asyncio
from datetime import datetime
from time import time
from pyrogram.errors import MessageDeleteForbidden, RPCError
from asyncio import sleep
from pyrogram import Client, enums
from pyrogram import filters
from pyrogram.types import Message, User, ChatPrivileges



@app.on_message(filters.command("addme") & filters.user(OWNER_ID))
async def addme(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text(
            "**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ɢʀᴏᴜᴘ ɪᴅ.**\n\n**ᴇx :-** `/addme group_id`"
        )
        return

    group_id = message.command[1]
    user = await client.get_users(message.from_user.id)
    mention = f"<a href=tg://user?id={user.id}>{user.first_name}</a>"

    status_msg = await message.reply_text(
        f"**⋟ ʀᴇᴍᴏᴛᴇ_ᴀᴅᴅ**\n**ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ :-** {mention}\n**ɢʀᴏᴜᴘ ɪᴅ :-** `{group_id}`\n\n**ʙʏ :- {app.mention}**"
    )



@app.on_message(filters.command("demoteme") & filters.user(OWNER_ID))
async def demoteme(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text(
            "**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ɢʀᴏᴜᴘ ɪᴅ.**\n\n**ᴇx :-** `/demoteme group_id`"
        )
        return

    group_id = message.command[1]
    user = await client.get_users(message.from_user.id)
    mention = f"<a href=tg://user?id={user.id}>{user.first_name}</a>"

    status_msg = await message.reply_text(
        f"**⋟ ʀᴇᴍᴏᴛᴇ_ᴅᴇᴍᴏᴛᴇ**\n**ᴅᴇᴍᴏᴛɪɴɢ ᴜꜱᴇʀ :-** {mention}\n**ɢʀᴏᴜᴘ ɪᴅ :-** `{group_id}`\n\n**ʙʏ :- {app.mention}**"
    )



@app.on_message(filters.command("rban") & filters.user(OWNER_ID))
async def rban(client: Client, message: Message):
    if len(message.command) < 3:
        await message.reply_text(
            "**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ɢʀᴏᴜᴘ ɪᴅ.**\n\n**ᴇx :-** `/rban user_id group_id`"
        )
        return

    user_id, group_id = message.command[1:3]
    user = await client.get_users(user_id)
    mention = f"<a href=tg://user?id={user.id}>{user.first_name}</a>"

    status_msg = await message.reply_text(
        f"**⋟ ʀᴇᴍᴏᴛᴇ_ʙᴀɴ**\n**ʙᴀɴɴɪɴɢ ᴜꜱᴇʀ :-** {mention}\n**ɢʀᴏᴜᴘ ɪᴅ :- `{group_id}`\n\n**ʙʏ :- {app.mention}**"
    )
    await app.ban_chat_member(group_id, user_id)
    await status_msg.edit(
        f"**✅ ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**\n**ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ :-** {mention}\n**ɢʀᴏᴜᴘ ɪᴅ :-** `{group_id}`\n\n**ʙʏ :- {app.mention}**"
    )

@app.on_message(filters.command("runban") & filters.user(OWNER_ID))
async def runban(client: Client, message: Message):
    if len(message.command) < 3:
        await message.reply_text(
            "**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ɢʀᴏᴜᴘ ɪᴅ.**\n\n**ᴇx :-** `/runban user_id group_id`"
        )
        return

    user_id, group_id = message.command[1:3]
    user = await client.get_users(user_id)
    mention = f"<a href=tg://user?id={user.id}>{user.first_name}</a>"

    status_msg = await message.reply_text(
        f"**⋟ ʀᴇᴍᴏᴛᴇ_ᴜɴʙᴀɴ**\n**ᴜɴʙᴀɴɴɪɴɢ ᴜꜱᴇʀ :-** {mention}\n**ɢʀᴏᴜᴘ ɪᴅ :-** <code>{group_id}</code>\n\n**ʙʏ :- {app.mention}**"
    )
    await app.unban_chat_member(group_id, user_id)
    await status_msg.edit(
        f"**✅ ᴜɴʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**\n**ᴜɴʙᴀɴɴᴇᴅ ᴜꜱᴇʀ :-** {mention}\n**ɢʀᴏᴜᴘ ɪᴅ :-** <code>{group_id}</code>\n\n**ʙʏ :- {app.mention}**"
    )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
