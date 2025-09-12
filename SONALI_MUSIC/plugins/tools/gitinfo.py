# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from SONALI_MUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("`/git TEAMPURVI`")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
✿ ᴜsᴇʀɴᴀᴍᴇ: {username}
✿ ʙɪᴏ : {bio}
✿ ʟɪɴᴋ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({url})
✿ ᴄᴏᴍᴩᴀɴʏ : {company}
✿ ᴄʀᴇᴀᴛᴇᴅ ᴏɴ : {created_at}
✿ ʀᴇᴩᴏsɪᴛᴏʀɪᴇs : {repositories}
✿ ʙʟᴏɢ : {blog}
✿ ʟᴏᴄᴀᴛɪᴏɴ : {location}
✿ ғᴏʟʟᴏᴡᴇʀs : {followers}
✿ ғᴏʟʟᴏᴡɪɴɢ : {following}"""

            except Exception as e:
                print(str(e))
                pass


    close_button = InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
