# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import Client, filters
import requests
from SONALI_MUSIC import app

def chunk_string(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

@app.on_message(filters.command("allrepo"))
async def all_repo_command(client, message):
    try:
        
        if len(message.command) > 1:
            github_username = message.command[1]
            
            repo_info = get_all_repository_info(github_username)
            
            chunked_repo_info = chunk_string(repo_info, 4000)  
         
            for chunk in chunked_repo_info:
                await message.reply_text(chunk)
        else:
            await message.reply_text("**ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ɢɪᴛʜᴜʙ ᴜsᴇʀɴᴀᴍᴇ ᴀғᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ.**")
    except Exception as e:
        await message.reply_text(f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴜᴅ :-** {str(e)}")

def get_all_repository_info(github_username):
    github_api_url = f"https://api.github.com/users/{github_username}/repos"

    response = requests.get(github_api_url)
    data = response.json()

    repo_info = "\n\n".join([
        f"**ʀᴇᴘᴏsɪᴛᴏʀʏ :-** {repo['full_name']}\n"
        f"**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ :-** {repo['description']}\n"
        f"**sᴛᴀʀs :-** {repo['stargazers_count']}\n"
        f"**ғᴏʀᴋs :-** {repo['forks_count']}\n"
        f"**ʀᴇᴘᴏ ᴜʀʟ :-** {repo['html_url']}"
        for repo in data
    ])

    return repo_info

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
