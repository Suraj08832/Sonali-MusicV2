# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import filters
from pyrogram.enums import ChatType, ChatMemberStatus
from strings import get_string
from SONALI_MUSIC import app
from SONALI_MUSIC.utils import SonaBin
from SONALI_MUSIC.utils.database import get_assistant, get_lang
from SONALI_MUSIC.core.call import Sona

from pyrogram.types import Message
from SONALI_MUSIC.core.call import SONA
from SONALI_MUSIC.utils.admin_filters import admin_filter


async def is_admin(_, __, message):
    try:
        chat_member = await message.chat.get_member(message.from_user.id)
        return chat_member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
    except:
        return False


@app.on_message(
    filters.command(
        ["vcuser", "vcusers", "vcmember", "vcmembers", "cu", "cm"],
        prefixes=["/", "!", ".", "V", "v"]
    ) & filters.create(is_admin)
)
async def vc_members(client, message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    msg = await message.reply_text(_["V_C_1"])
    userbot = await get_assistant(message.chat.id)
    TEXT = ""

    try:
        async for m in userbot.get_call_members(message.chat.id):
            chat_id = m.chat.id
            username = m.chat.username
            is_hand_raised = m.is_hand_raised
            is_video_enabled = m.is_video_enabled
            is_left = m.is_left
            is_screen_sharing_enabled = m.is_screen_sharing_enabled
            is_muted = bool(m.is_muted and not m.can_self_unmute)
            is_speaking = not m.is_muted

            if m.chat.type != ChatType.PRIVATE:
                title = m.chat.title
            else:
                try:
                    title = (await client.get_users(chat_id)).mention
                except:
                    title = m.chat.first_name

            TEXT += _["V_C_2"].format(
                title,
                chat_id,
                username,
                is_video_enabled,
                is_screen_sharing_enabled,
                is_hand_raised,
                is_muted,
                is_speaking,
                is_left,
            )
            TEXT += "\n\n"

        if len(TEXT) < 4000:
            await msg.edit(TEXT or _["V_C_3"])
        else:
            link = await SonaBin(TEXT)
            await msg.edit(
                _["V_C_4"].format(link),
                disable_web_page_preview=True,
            )
    except ValueError:
        await msg.edit(_["V_C_5"])




@app.on_message(filters.command("volume") & filters.group & admin_filter)
async def set_volume(client, message: Message):
    chat_id = message.chat.id

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text(
            "**⚠️ ᴜsᴀɢᴇ :-** `/volume 1-200`"
        )
    
    try:
        volume_level = int(args[1])
    except ValueError:
        return await message.reply_text(
            "**❌ ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ. ᴘʟᴇᴀsᴇ ᴜsᴇ :-** `/volume 1-200`"
        )
    
    if volume_level == 0:
        return await message.reply_text(
            "**🔇 ᴜsᴇ** `/mute` **ᴛᴏ ᴍᴜᴛᴇ ᴛʜᴇ sᴛʀᴇᴀᴍ**"
        )
    
    if not 1 <= volume_level <= 200:
        return await message.reply_text(
            "**⚠️ ᴠᴏʟᴜᴍᴇ ᴍᴜsᴛ ʙᴇ ʙᴇᴛᴡᴇᴇɴ 1 ᴀɴᴅ 200**"
        )
    
    if chat_id >= 0:
        return await message.reply_text(
            "**❌ ᴠᴏʟᴜᴍᴇ ᴄᴏɴᴛʀᴏʟ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ ʙᴀsɪᴄ ɢʀᴏᴜᴘs**"
        )
    
    try:
        await SONA.change_volume(chat_id, volume_level)
        await message.reply_text(
            f"**🔊 sᴛʀᴇᴀᴍ ᴠᴏʟᴜᴍᴇ sᴇᴛ ᴛᴏ :-** `{volume_level}`\n**└ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :- {message.from_user.mention} 🥀**"
        )
    except Exception as e:
        await message.reply_text(
            f"**❌ ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴠᴏʟᴜᴍᴇ. ᴇʀʀᴏʀ :-** {e}"
        )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
