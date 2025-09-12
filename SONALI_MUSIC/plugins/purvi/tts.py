# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import Client, filters
from gtts import gTTS
from SONALI_MUSIC import app


@app.on_message(filters.command('tts'))
async def text_to_speech(client, message):
    try:
      
        if len(message.text.split()) < 2:
            await message.reply_text(
                "**ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ғᴏʀ ᴛᴛs.** \n\n**ᴜsᴀɢᴇ :** `/tts i love you`"
            )
            return

        
        text = message.text.split(' ', 1)[1]

        
        tts = gTTS(text=text, lang='hi')
        file_name = "speech.mp3"
        tts.save(file_name)

        
        await app.send_audio(chat_id=message.chat.id, audio=file_name)

    except Exception as e:
        
        await message.repl
        

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
