# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from SONALI_MUSIC import app
from pyrogram import filters, enums
from pyrogram.types import ChatPermissions
from SONALI_MUSIC.utils.Sona_BAN import admin_filter

@app.on_message(filters.command("unmuteall") & admin_filter)
async def unmute_all(_, msg):
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    

    bot = await app.get_chat_member(chat_id, user_id)
    if not (bot.privileges and bot.privileges.can_restrict_members):
        return await msg.reply_text("**⚠️ ɴᴏ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴍᴇᴍʙᴇʀs.**")

    count = 0
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
        try:
            await app.restrict_chat_member(
                chat_id,
                m.user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_polls=True,
                    can_add_web_page_previews=True,
                    can_invite_users=True
                )
            )
            count += 1
            print(f"**✅ ᴜɴᴍᴜᴛᴇᴅ {m.user.mention}**")
        except Exception as e:
            print(f"❌ {m.user.id} - {e}")

    if count == 0:
        await msg.reply_text("**😶 ɴᴏ ᴍᴜᴛᴇᴅ ᴍᴇᴍʙᴇʀs ғᴏᴜɴᴅ.**")
    else:
        await msg.reply_text(f"**🔊 ᴜɴᴍᴜᴛᴇᴅ `{count}` ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ᴄʜᴀᴛ ✅**")

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
