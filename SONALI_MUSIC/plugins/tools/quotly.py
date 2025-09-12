# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import os
import base64
import aiohttp
from random import choice
from pyrogram import filters
from pyrogram.types import Message

from SONALI_MUSIC import app  

API_URL = "https://bot.lyo.su/quote/generate"

class Quotly:
    _entities = {
        "phone_number": "phone_number",
        "mention": "mention",
        "bold": "bold",
        "cashtag": "cashtag",
        "strikethrough": "strikethrough",
        "hashtag": "hashtag",
        "email": "email",
        "text_mention": "text_mention",
        "underline": "underline",
        "url": "url",
        "text_link": "text_link",
        "bot_command": "bot_command",
        "code": "code",
        "pre": "pre",
    }

    async def _format_quote(self, message: Message, reply=None, sender=None, type_="private"):
        reply_msg = {}
        if reply:
            reply_msg = {
                "name": reply.from_user.first_name if reply.from_user else "Deleted",
                "text": reply.text or "",
                "chatId": reply.chat.id if reply.chat else None,
            }

        from_user = message.from_user or None
        if sender:
            from_user = sender

        entities = []
        if message.entities:
            for e in message.entities:
                etype = str(e.type)
                if etype in self._entities:
                    entities.append({"type": self._entities[etype], "offset": e.offset, "length": e.length})

        msg_data = {
            "entities": entities,
            "chatId": message.chat.id,
            "avatar": True,
            "from": {
                "id": from_user.id if from_user else None,
                "first_name": from_user.first_name if from_user else "Deleted Account",
                "last_name": from_user.last_name if from_user else None,
                "username": from_user.username if from_user else None,
                "language_code": "en",
                "title": from_user.first_name if from_user else "Unknown",
                "name": from_user.first_name if from_user else "Unknown",
                "type": type_,
            },
            "text": message.text or "",
            "replyMessage": reply_msg,
        }
        return msg_data

    async def create_quotly(self, messages, reply=None, sender=None, bg="#1b1429", file_name="quote.webp"):
        if not isinstance(messages, list):
            messages = [messages]

        content = {
            "type": "quote",
            "format": "webp",
            "backgroundColor": bg,
            "width": 512,
            "height": 768,
            "scale": 2,
            "messages": [await self._format_quote(m, reply=reply, sender=sender) for m in messages],
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, json=content) as resp:
                data = await resp.json()
                if data.get("ok"):
                    image = base64.b64decode(data["result"]["image"])
                    with open(file_name, "wb") as f:
                        f.write(image)
                    return file_name
                raise Exception(str(data))

quotly = Quotly()

@app.on_message(filters.command("q") & filters.reply)
async def quott_(client, message: Message):
    msg = await message.reply("⚡ Making Quote...")
    reply = message.reply_to_message

    args = message.text.split(None, 1)
    arg = args[1].lower() if len(args) > 1 else None

    replied_to = None
    bg = "#1b1429"

    if arg in ["r", "reply"] and reply.reply_to_message:
        replied_to = reply.reply_to_message
    elif arg == "random":
        bg = choice(["#1b1429", "#2a2139", "#ff006e", "#8338ec", "#3a86ff"])

    try:
        file = await quotly.create_quotly(reply, bg=bg, reply=replied_to)
    except Exception as e:
        return await msg.edit(str(e))

    await message.reply_document(file)
    os.remove(file)
    await msg.delete()
                
            
# ---------------------------------------------------------------------------------

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
