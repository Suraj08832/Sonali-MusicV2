# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app


@app.on_message(filters.command(["unpinall"]) & filters.group)
async def unpinall_command(client, message):
    chat = message.chat
    admin_id = message.from_user.id
    member = await chat.get_member(admin_id)

    if member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER] \
       or not member.privileges.can_pin_messages:
        return await message.reply_text(
            "**⚠ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴᴘɪɴ ᴍᴇssᴀɢᴇs.**"
        )

    await message.reply_text(
        "**❓ ᴀʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜɴᴘɪɴ ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ᴄʜᴀᴛ?**",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("✔ ʏᴇs", callback_data="unpin=yes"),
                InlineKeyboardButton("✖ ɴᴏ", callback_data="unpin=no")
            ]]
        )
    )


@app.on_callback_query(filters.regex(r"^unpin=(yes|no)$"))
async def unpin_callback(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    action = CallbackQuery.data.split("=")[1]

    if action == "yes":
        await client.unpin_all_chat_messages(chat_id)
        text = "**✅ ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴᴘɪɴɴᴇᴅ!**"
    else:
        text = "**❌ ᴏᴋᴀʏ, ɪ ᴡɪʟʟ ɴᴏᴛ ᴜɴᴘɪɴ ᴀɴʏᴛʜɪɴɢ.**"

    await CallbackQuery.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]]
        )
    )


# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
