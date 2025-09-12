# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from SONALI_MUSIC import app
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SONALI_MUSIC.utils.Sona_BAN import admin_filter

@app.on_message(filters.command("unbanall") & admin_filter)
async def unban_all(_, msg):
    chat_id = msg.chat.id

    me = await app.get_me()
    BOT_ID = me.id

    try:
        bot = await app.get_chat_member(chat_id, BOT_ID)
        bot_permission = bot.privileges.can_restrict_members if bot.privileges else False

        if not bot_permission:
            await msg.reply_text(
                "**ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ.**",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="stop")]]
                ),
            )
            return

        banned_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
            banned_users.append(m.user.id)

        if not banned_users:
            await msg.reply_text("**ɴᴏ ʙᴀɴɴᴇᴅ ᴜsᴇʀs ᴛᴏ ᴜɴʙᴀɴ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.**")
            return

        unbanned_count = 0
        for user_id in banned_users:
            try:
                await app.unban_chat_member(chat_id, user_id)
                unbanned_count += 1
            except Exception:
                pass

        await msg.reply_text(
            f"**ᴜɴʙᴀɴɴᴇᴅ `{unbanned_count}` ᴜsᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ✅**",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="stop")]]
            ),
        )

    except Exception as e:
        await msg.reply_text(
            f"**sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ :-** `{e}`",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="stop")]]
            ),
        )

@app.on_callback_query(filters.regex("^stop$"))
async def stop_callback(_, query):
    await query.message.delete()

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
