# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import filters
import random
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from SONALI_MUSIC.plugins.tools.pretenderdb import (
    impo_off, impo_on, check_pretender,
    add_userdata, get_userdata, usr_data
)
from SONALI_MUSIC.utils.admin_filters import admin_filter


PURVI = [
    "https://files.catbox.moe/x5lytj.jpg",
    "https://files.catbox.moe/psya34.jpg",
    "https://files.catbox.moe/leaexg.jpg",
    "https://files.catbox.moe/b0e4vk.jpg",
    "https://files.catbox.moe/1b1wap.jpg",
    "https://files.catbox.moe/ommjjk.jpg",
    "https://files.catbox.moe/onurxm.jpg",
    "https://files.catbox.moe/97v75k.jpg",
    "https://files.catbox.moe/t833zy.jpg",
    "https://files.catbox.moe/472piq.jpg",
    "https://files.catbox.moe/qwjeyk.jpg",
    "https://files.catbox.moe/t0hopv.jpg",
    "https://files.catbox.moe/u5ux0j.jpg",
    "https://files.catbox.moe/h1yk4w.jpg",
    "https://files.catbox.moe/gl5rg8.jpg",
]

@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not message.from_user:
        return
        
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
        
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**✽ ᴜsᴇʀ sʜᴏʀᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ✽**
━━━━━━━━━━━━━━━  
**● ɴᴀᴍᴇ :-** {message.from_user.mention}
**● ᴜsᴇʀ ɪᴅ :-** {message.from_user.id}
━━━━━━━━━━━━━━━  \n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        )
        msg += """
**❖ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ ⏤͟͟͞͞★**
━━━━━━━━━━━━━━━  
**● ʙᴇғᴏʀᴇ :-** {bef}
**● ᴀғᴛᴇʀ :-** {aft}
━━━━━━━━━━━━━━━  \n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
        
    if first_name != message.from_user.first_name:
        msg += """
**❖ ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ ⏤͟͟͞͞★**
━━━━━━━━━━━━━━━  
**● ʙᴇғᴏʀᴇ :-** {bef}
**● ᴀғᴛᴇʀ :-** {aft}
━━━━━━━━━━━━━━━  \n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
        
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
        lastname_after = message.from_user.last_name or "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
        msg += """
**❖ ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ ⏤͟͟͞͞★**
━━━━━━━━━━━━━━━  
**● ʙᴇғᴏʀᴇ :-** {bef}
**● ᴀғᴛᴇʀ :-** {aft}
━━━━━━━━━━━━━━━  \n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
        
    if msg != "":
        photo = random.choice(PURVI)
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton("✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/{app.username}?startgroup=true")]]
        )
        await message.reply_photo(photo=photo, caption=msg, reply_markup=buttons)

@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot & admin_filter)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ :-**\n\n**ᴇɴᴀʙʟᴇ :-** `/imposter enable`\n**ᴅɪsᴀʙʟᴇ :-** `/imposter disable`")
    
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ :-** {message.chat.title}")
            
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ :-** {message.chat.title}")
            
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
