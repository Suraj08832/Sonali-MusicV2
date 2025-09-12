# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from SONALI_MUSIC.utils.mongo import impdb


async def usr_data(user_id: int) -> bool:
    user = await impdb.find_one({"user_id": user_id})
    return bool(user)


async def get_userdata(user_id: int):
    user = await impdb.find_one({"user_id": user_id})
    return user["username"], user["first_name"], user["last_name"]


async def add_userdata(user_id: int, username, first_name, last_name):
    await impdb.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
            }
        },
        upsert=True,
    )


async def check_pretender(chat_id: int) -> bool:
    chat = await impdb.find_one({"chat_id_toggle": chat_id})
    return bool(chat)


async def impo_on(chat_id: int):
    await impdb.insert_one({"chat_id_toggle": chat_id})


async def impo_off(chat_id: int):
    await impdb.delete_one({"chat_id_toggle": chat_id})

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
