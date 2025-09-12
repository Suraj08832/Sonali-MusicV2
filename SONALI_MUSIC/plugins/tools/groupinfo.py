# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from SONALI_MUSIC import app

@app.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Please provide a group username. Example: `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"**➖➖➖➖➖➖➖**\n"
        f"**➲ GROUP NAME :** {group.title} ✅\n"
        f"**➲ GROUP ID :** {group.id}\n"
        f"**➲ TOTAL MEMBERS :** {total_members}\n"
        f"**➲ DESCRIPTION :** {group_description or 'N/A'}\n"
        f"**➲ USERNAME :** {group_username}\n"
       
        f"**➖➖➖➖➖➖➖**"
    )
    
    await message.reply(response_text)






@app.on_message(filters.command("status") & filters.group)
async def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = (
        f"**ɢʀᴏᴜᴘ ɪɴғᴏʀᴍᴀᴛɪᴏɴ**\n\n"
        f"**ɢʀᴏᴜᴘ ɪᴅ :-** `{chat.id}`\n"
        f"**ᴛɪᴛʟᴇ :-** **{chat.title}**\n"
        f"**ᴛʏᴘᴇ :-** `{chat.type}`\n"
    )

    # Check if the group has a username
    if chat.username:
        status_text += f"**ᴜsᴇʀɴᴀᴍᴇ :-** @{chat.username}\n"
    else:
        status_text += "**ᴜsᴇʀɴᴀᴍᴇ :-** None\n"

    # Send the response
    await message.reply_text(status_text)
    

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
