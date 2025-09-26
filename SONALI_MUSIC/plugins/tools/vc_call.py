# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================


import asyncio
from logging import getLogger
from typing import Dict, Set
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.raw import functions
from SONALI_MUSIC import app
from SONALI_MUSIC.utils.database import get_assistant

LOGGER = getLogger(__name__)

vc_active_users: Dict[int, Set[int]] = {}
active_vc_chats: Set[int] = set()

async def delete_after_delay(message, delay: int = 5):
    
    try:
        await asyncio.sleep(delay)
        await message.delete()
    except Exception as e:
        LOGGER.debug(f"**» ᴄᴏᴜʟᴅ ɴᴏᴛ ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs :-** {e}")

async def get_group_call_participants(userbot, peer):
    try:
        full_chat = await userbot.invoke(functions.channels.GetFullChannel(channel=peer))
        if not hasattr(full_chat.full_chat, "call") or not full_chat.full_chat.call:
            return []
        call = full_chat.full_chat.call
        participants = await userbot.invoke(
            functions.phone.GetGroupParticipants(
                call=call, ids=[], sources=[], offset="", limit=100
            )
        )
        return participants.participants
    except:
        return []

async def monitor_vc_chat(chat_id):
    userbot = await get_assistant(chat_id)
    if not userbot:
        return

    while chat_id in active_vc_chats:
        try:
            peer = await userbot.resolve_peer(chat_id)
            participants_list = await get_group_call_participants(userbot, peer)
            new_users = set()
            for p in participants_list:
                if hasattr(p, "peer") and hasattr(p.peer, "user_id"):
                    new_users.add(p.peer.user_id)

            current_users = vc_active_users.get(chat_id, set())
            joined = new_users - current_users
            left = current_users - new_users

            
            for user_id in joined:
                await handle_user_join(chat_id, user_id, userbot)

            
            for user_id in left:
                await handle_user_leave(chat_id, user_id, userbot)

            vc_active_users[chat_id] = new_users

        except Exception as e:
            LOGGER.error(f"**» ᴇʀʀᴏʀ ᴍᴏɴɪᴛᴏʀɪɴɢ ᴠᴄ ғᴏʀ ᴄʜᴀᴛ** `{chat_id}` **:-** {e}")

        await asyncio.sleep(2) 

async def check_and_monitor_vc(chat_id):
    if chat_id in active_vc_chats:
        return
    userbot = await get_assistant(chat_id)
    if not userbot:
        return
    try:
        peer = await userbot.resolve_peer(chat_id)
        participants = await get_group_call_participants(userbot, peer)
        if participants:
            active_vc_chats.add(chat_id)
            asyncio.create_task(monitor_vc_chat(chat_id))
    except:
        pass

async def handle_user_join(chat_id, user_id, userbot):
    try:
        user = await userbot.get_users(user_id)
        mention = f'<a href="tg://user?id={user_id}">{user.first_name}</a>'
        username = f"@{user.username}" if user.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"

        text = (
            f"🎤 **ᴜsᴇʀ ᴊᴏɪɴᴇᴅ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ**\n\n"
            f"👤 **ɴᴀᴍᴇ :-** {mention}\n"
            f"🔗 **ᴜsᴇʀɴᴀᴍᴇ** :- {username}\n"
            f"🆔 **ɪᴅ :-** `{user_id}`\n\n"
            f"**❖ ᴛʜᴀɴᴋs ғᴏʀ ᴊᴏɪɴɪɴɢ 😁**"
        )

        sent_msg = await app.send_message(chat_id, text)
        asyncio.create_task(delete_after_delay(sent_msg, 5))
    except Exception as e:
        LOGGER.error(f"**» ᴇʀʀᴏʀ sᴇɴᴅɪɴɢ ᴠᴄ ᴊᴏɪɴ ᴍsɢ :-** {e}")

async def handle_user_leave(chat_id, user_id, userbot):
    try:
        user = await userbot.get_users(user_id)
        mention = f'<a href="tg://user?id={user_id}">{user.first_name}</a>'
        username = f"@{user.username}" if user.username else "**ɴᴏ ᴜsᴇʀɴᴀᴍᴇ**"

        text = (
            f"🚪 **ᴜsᴇʀ ʟᴇғᴛ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ**\n\n"
            f"👤 **ɴᴀᴍᴇ :-** {mention}\n"
            f"🔗 **ᴜsᴇʀɴᴀᴍᴇ :-** {username}\n"
            f"🆔 **ɪᴅ :-** `{user_id}`\n\n"
            f"**❖ ʙʏᴇ ʙʏᴇ ᴠɪsɪᴛ ᴀɢᴀɪɴ 👋**"
        )

        sent_msg = await app.send_message(chat_id, text)
        asyncio.create_task(delete_after_delay(sent_msg, 5))
    except Exception as e:
        LOGGER.error(f"**» ᴇʀʀᴏʀ sᴇɴᴅɪɴɢ ᴠᴄ ʟᴇᴀᴠᴇ ᴍsɢ :-** {e}")


@app.on_message(filters.group)
async def auto_vc_logger_trigger(_, message: Message):
    chat_id = message.chat.id
    asyncio.create_task(check_and_monitor_vc(chat_id))


# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
