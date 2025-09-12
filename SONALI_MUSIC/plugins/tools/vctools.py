# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from SONALI_MUSIC import app
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    text = "**🫣 ᴠɪᴅᴇᴏ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ 😆**"
    add_link = f"https://t.me/{app.username}?startgroup=true"
    reply_text = f"{text}"

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="๏ ᴊσɪη ᴠᴄ ๏", url=add_link)]
    ])

    await msg.reply(reply_text, reply_markup=reply_markup)



@app.on_message(filters.video_chat_ended)
async def brah2(_, msg: Message):
    text = "**😤 ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ 🙁**"
    add_link = f"https://t.me/{app.username}?startgroup=true"
    reply_text = f"{text}"

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="๏ ᴧᴅᴅ ϻє вᴧвყ ๏", url=add_link)]
    ])

    await msg.reply(reply_text, reply_markup=reply_markup)
    
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"➠ {message.from_user.mention}\n\n**๏ ɪɴᴠɪᴛɪɴɢ ɪɴ ᴠᴄ ᴛᴏ ๏**\n\n**➠ **"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass

    try:
        invite_link = await app.export_chat_invite_link(message.chat.id)
        add_link = f"https://t.me/{app.username}?startgroup=true"
        reply_text = f"{text} 🤭🤭"

        await message.reply(reply_text, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text= "๏ ᴊσɪη ᴠᴄ ๏", url=add_link)],
        ]))
    except Exception as e:
        print(f"Error: {e}")


# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
