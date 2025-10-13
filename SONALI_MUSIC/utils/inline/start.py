# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

from pyrogram.types import InlineKeyboardButton

import config
from SONALI_MUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton("˹ ᴧʙσυт ˼", callback_data="ALLBOT_CP"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="MAIN_CP"),
        ],
    ]
    return buttons

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/Sonali-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
