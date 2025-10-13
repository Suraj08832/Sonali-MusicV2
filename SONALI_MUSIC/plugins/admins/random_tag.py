# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @brahix
# =======================================================

from SONALI_MUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " ** ʜᴇʏ ʙᴀʙʏ ᴋᴀʜᴀ ʜᴏ 🤗** ",
           " ** ᴏʏᴇ sᴏ ɢʏᴇ ᴋʏᴀ ᴏɴʟɪɴᴇ ᴀᴀᴏ 😊** ",
           " ** ᴠᴄ ᴄʜᴀʟᴏ ʙᴀᴛᴇɴ ᴋᴀʀᴛᴇ ʜᴀɪɴ ᴋᴜᴄʜ ᴋᴜᴄʜ 😃** ",
           " ** ᴋʜᴀɴᴀ ᴋʜᴀ ʟɪʏᴇ ᴊɪ..?? 🥲** ",
           " ** ɢʜᴀʀ ᴍᴇ sᴀʙ ᴋᴀɪsᴇ ʜᴀɪɴ ᴊɪ 🥺** ",
           " ** ᴘᴛᴀ ʜᴀɪ ʙᴏʜᴏᴛ ᴍɪss ᴋᴀʀ ʀʜɪ ᴛʜɪ ᴀᴀᴘᴋᴏ 🤭** ",
           " ** ᴏʏᴇ ʜᴀʟ ᴄʜᴀʟ ᴋᴇsᴀ ʜᴀɪ..?? 🤨** ",
           " ** ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ..?? 🙂** ",
           " ** ᴀᴀᴘᴋᴀ ɴᴀᴍᴇ ᴋʏᴀ ʜᴀɪ..?? 🥲** ",
           " ** ɴᴀsᴛᴀ ʜᴜᴀ ᴀᴀᴘᴋᴀ..?? 😋** ",
           " ** ᴍᴇʀᴇ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴍᴇ ᴋɪᴅɴᴀᴘ ᴋʀ ʟᴏ 😍** ",
           " ** ᴀᴀᴘᴋɪ ᴘᴀʀᴛɴᴇʀ ᴀᴀᴘᴋᴏ ᴅʜᴜɴᴅ ʀʜᴇ ʜᴀɪɴ ᴊʟᴅɪ ᴏɴʟɪɴᴇ ᴀʏɪᴀᴇ 😅** ",
           " ** ᴍᴇʀᴇ sᴇ ᴅᴏsᴛɪ ᴋʀᴏɢᴇ..?? 🤔** ",
           " ** ᴇᴅʜᴀʀ ᴅᴇᴋʜᴏ ᴋʏᴀ ʜᴀɪ @about_brahix ...😘** ",
           " ** ʙᴀʙᴜ ʏᴇ ᴅᴇᴋʜᴏ ᴀʟᴘʜᴀ ᴋᴀ ᴀᴅᴅᴀ @Oye_Careless... 😎** ",
           " ** sᴏɴᴇ ᴄʜᴀʟ ɢʏᴇ ᴋʏᴀ 🙄** ",
           " ** ᴇᴋ sᴏɴɢ ᴘʟᴀʏ ᴋʀᴏ ɴᴀ ᴘʟss 😕** ",
           " ** ᴀᴀᴘ ᴋᴀʜᴀ sᴇ ʜᴏ..?? 🙃** ",
           " ** ʜᴇʟʟᴏ ᴊɪ ɴᴀᴍᴀsᴛᴇ 😛** ",
           " ** ʜᴇʟʟᴏ ʙᴀʙʏ ᴋᴋʀʜ..? 🤔** ",
           " ** ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ᴡʜᴏ ɪs ᴍʏ ᴏᴡɴᴇʀ.? ☺️** ",
           " ** ᴄʜʟᴏ ᴋᴜᴄʜ ɢᴀᴍᴇ ᴋʜᴇʟᴛᴇ ʜᴀɪɴ.🤗** ",
           " ** ᴀᴜʀ ʙᴀᴛᴀᴏ ᴋᴀɪsᴇ ʜᴏ ʙᴀʙʏ 😇** ",
           " ** ᴛᴜᴍʜᴀʀɪ ᴍᴜᴍᴍʏ ᴋʏᴀ ᴋᴀʀ ʀᴀʜɪ ʜᴀɪ 🤭** ",
           " ** ᴍᴇʀᴇ sᴇ ʙᴀᴛ ɴᴏɪ ᴋʀᴏɢᴇ 🥺** ",
           " ** ᴏʏᴇ ᴘᴀɢᴀʟ ᴏɴʟɪɴᴇ ᴀᴀ ᴊᴀ 😶** ",
           " ** ᴀᴀᴊ ʜᴏʟɪᴅᴀʏ ʜᴀɪ ᴋʏᴀ sᴄʜᴏᴏʟ ᴍᴇ..?? 🤔** ",
           " ** ᴏʏᴇ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 😜** ",
           " ** sᴜɴᴏ ᴇᴋ ᴋᴀᴍ ʜᴀɪ ᴛᴜᴍsᴇ 🙂** ",
           " ** ᴋᴏɪ sᴏɴɢ ᴘʟᴀʏ ᴋʀᴏ ɴᴀ 😪** ",
           " ** ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜ ☺** ",
           " ** ᴍᴇʀᴀ ʙᴀʙᴜ ɴᴇ ᴛʜᴀɴᴀ ᴋʜᴀʏᴀ ᴋʏᴀ..? 🙊** ",
           " ** sᴛᴜᴅʏ ᴄᴏᴍᴘʟᴇᴛᴇ ʜᴜᴀ?? 😺** ",
           " ** ʙᴏʟᴏ ɴᴀ ᴋᴜᴄʜ ʏʀʀ 🥲** ",
           " ** sᴏɴᴀʟɪ ᴋᴏɴ ʜᴀɪ...?? 😅** ",
           " ** ᴛᴜᴍʜᴀʀɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ..? 😅** ",
           " ** ᴍᴜᴍᴍʏ ᴀᴀ ɢʏɪ ᴋʏᴀ 😆** ",
           " ** ᴏʀ ʙᴀᴛᴀᴏ ʙʜᴀʙʜɪ ᴋᴀɪsɪ ʜᴀɪ 😉** ",
           " ** ɪ ʟᴏᴠᴇ ʏᴏᴜ 💚** ",
           " ** ᴅᴏ ʏᴏᴜ ʟᴏᴠᴇ ᴍᴇ..? 👀** ",
           " ** ʀᴀᴋʜɪ ᴋᴀʙ ʙᴀɴᴅ ʀᴀʜɪ ʜᴏ..?? 🙉** ",
           " ** ᴇᴋ sᴏɴɢ sᴜɴᴀᴜ..? 😹** ",
           " ** ᴏɴʟɪɴᴇ ᴀᴀ ᴊᴀ ʀᴇ sᴏɴɢ sᴜɴᴀ ʀᴀʜɪ ʜᴜ 😻** ",
           " ** ɪɴsᴛᴀɢʀᴀᴍ ᴄʜᴀʟᴀᴛᴇ ʜᴏ..?? 🙃** ",
           " ** ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ ᴅᴏɢᴇ ᴀᴘɴᴀ ᴛᴜᴍ..? 😕** ",
           " ** ᴛᴜᴍʜᴇ ᴋᴏɴ sᴀ ᴍᴜsɪᴄ sᴜɴɴᴀ ᴘᴀsᴀɴᴅ ʜᴀɪ..? 🙃** ",
           " ** sᴀʀᴀ ᴋᴀᴍ ᴋʜᴀᴛᴀᴍ ʜᴏ ɢʏᴀ ᴀᴀᴘᴋᴀ..? 🙃** ",
           " ** ᴋᴀʜᴀ sᴇ ʜᴏ ᴀᴀᴘ 😊** ",
           " ** sᴜɴᴏ ɴᴀ 🧐** ",
           " ** ᴍᴇʀᴀ ᴇᴋ ᴋᴀᴀᴍ ᴋᴀʀ ᴅᴏɢᴇ..? ♥️** ",
           " ** ʙʏ ᴛᴀᴛᴀ ᴍᴀᴛ ʙᴀᴀᴛ ᴋᴀʀɴᴀ ᴀᴀᴊ ᴋᴇ ʙᴀᴅ 😠** ",
           " ** ᴍᴏᴍ ᴅᴀᴅ ᴋᴀɪsᴇ ʜᴀɪɴ..? ❤** ",
           " ** ᴋʏᴀ ʜᴜᴀ..? 🤔** ",
           " ** ʙᴏʜᴏᴛ ʏᴀᴀᴅ ᴀᴀ ʀʜɪ ʜᴀɪ 😒** ",
           " ** ʙʜᴜʟ ɢʏᴇ ᴍᴜᴊʜᴇ 😏** ",
           " ** ᴊᴜᴛʜ ɴʜɪ ʙᴏʟɴᴀ ᴄʜᴀʜɪʏᴇ 🤐** ",
           " ** ᴋʜᴀ ʟᴏ ʙʜᴀᴡ ᴍᴀᴛ ᴋʀᴏ ʙᴀᴀᴛ 😒** ",
           " ** ᴋʏᴀ ʜᴜᴀ 😮** "
           " ** ʜɪɪ ʜᴏɪ ʜᴇʟʟᴏ 👀** ",
           " ** ᴀᴀᴘᴋᴇ ᴊᴀɪsᴀ ᴅᴏsᴛ ʜᴏ sᴀᴛʜ ᴍᴇ ғɪʀ ɢᴜᴍ ᴋɪs ʙᴀᴀᴛ ᴋᴀ 🙈** ",
           " ** ᴀᴀᴊ ᴍᴇ sᴀᴅ ʜᴏᴏɴ ☹️** ",
           " ** ᴍᴜsᴊʜsᴇ ʙʜɪ ʙᴀᴀᴛ ᴋᴀʀ ʟᴏ ɴᴀ 🥺** ",
           " ** ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴇ ʜᴏ 👀** ",
           " ** ᴋʏᴀ ʜᴀʟ ᴄʜᴀʟ ʜᴀɪ 🙂** ",
           " ** ᴋᴀʜᴀ sᴇ ʜᴏ ᴀᴀᴘ..?🤔** ",
           " ** ᴄʜᴀᴛᴛɪɴɢ ᴋᴀʀ ʟᴏ ɴᴀ..🥺** ",
           " ** ᴍᴇ ᴍᴀsᴏᴏᴍ ʜᴜ ɴᴀ 🥺** ",
           " ** ᴋᴀʟ ᴍᴀᴊᴀ ᴀʏᴀ ᴛʜᴀ ɴᴀ 😅** ",
           " ** ɢʀᴏᴜᴘ ᴍᴇ ʙᴀᴀᴛ ᴋʏᴜ ɴᴀʜɪ ᴋᴀʀᴛᴇ ʜᴏ 😕** ",
           " ** ᴀᴀᴘ ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴍᴇ ʜᴏ..? 👀** ",
           " ** ᴋɪᴛɴᴀ ᴄʜᴜᴘ ʀᴀʜᴛᴇ ʜᴏ ʏʀʀ 😼** ",
           " ** ᴀᴀᴘᴋᴏ ɢᴀɴᴀ ɢᴀɴᴇ ᴀᴀᴛᴀ ʜᴀɪ..? 😸** ",
           " ** ɢʜᴜᴍɴᴇ ᴄʜᴀʟᴏɢᴇ..?? 🙈** ",
           " ** ᴋʜᴜs ʀᴀʜᴀ ᴋᴀʀᴏ 🤞** ",
           " ** ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...? 🥰** ",
           " ** ᴋᴜᴄʜ ʙᴏʟ ᴋʏᴜ ɴʜɪ ʀᴀʜᴇ ʜᴏ.. 🥺** ",
           " ** ᴋᴜᴄʜ ᴍᴇᴍʙᴇʀs ᴀᴅᴅ ᴋᴀʀ ᴅᴏ 🥲** ",
           " ** sɪɴɢʟᴇ ʜᴏ ʏᴀ ᴍɪɴɢʟᴇ 😉** ",
           " ** ᴀᴀᴏ ᴘᴀʀᴛʏ ᴋᴀʀᴛᴇ ʜᴀɪɴ 🥳** ",
           " ** ʙɪᴏ ᴍᴇ ʟɪɴᴋ ʜᴀɪ ᴊᴏɪɴ ᴋᴀʀ ʟᴏ 🧐** ",
           " ** ᴍᴜᴊʜᴇ ʙʜᴜʟ ɢʏᴇ ᴋʏᴀ 🥺** ",
           " ** ʏᴀʜᴀ ᴀᴀ ᴊᴀᴏ @ALPHA_SAYS ᴍᴀsᴛɪ ᴋᴀʀᴇɴɢᴇ 🤭** ",
           " ** ᴛʀᴜᴛʜ ᴀɴᴅ ᴅᴀʀᴇ ᴋʜᴇʟᴏɢᴇ..? 😊** ",
           " ** ᴀᴀᴊ ᴍᴜᴍᴍʏ ɴᴇ ᴅᴀᴛᴀ ʏʀʀ 🥺** ",
           " ** ᴊᴏɪɴ ᴋᴀʀ ʟᴏ @brahix_support 🤗** ",
           " ** ᴇᴋ ᴅɪʟ ʜᴀɪ ᴇᴋ ᴅɪʟ ʜɪ ᴛᴏ ʜᴀɪ 😗** ",
           " ** ᴛᴜᴍʜᴀʀᴇ ᴅᴏsᴛ ᴋᴀʜᴀ ɢʏᴇ 🥺** ",
           " ** ᴍʏ ᴄᴜᴛᴇ ᴏᴡɴᴇʀ @PurviBots 🥰** ",
           " ** ᴋᴀʜᴀ ᴋʜᴏʏᴇ ʜᴏ ᴊᴀᴀɴ 😜** ",
           " ** ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ ʙʜᴜᴛ ʀᴀᴛ ʜᴏ ɢʏɪ 🥰** ",
           ]

VC_TAG = [
    "**ᴏʏᴇ ᴠᴄ ᴀᴀᴏ ɴᴀ ᴘʟs 😒**",
    "**ᴊᴏɪɴ ᴠᴄ ғᴀsᴛ ɪᴛs ɪᴍᴘᴏʀᴛᴀɴᴛ 😐**",
    "**ʙᴀʙʏ ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ғᴀsᴛ 🙄**",
    "**ᴄʜᴜᴘ ᴄʜᴀᴘ ᴠᴄ ᴘʀ ᴀᴀᴏ 🤫**",
    "**ᴍᴀɪɴ ᴠᴄ ᴍᴇ ᴛᴜᴍᴀʀᴀ ᴡᴀɪᴛ ᴋʀ ʀʜɪ 🥺**",
    "**ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ʙᴀᴀᴛ ᴋʀᴛᴇ ʜᴀɪ ☺️**",
    "**ʙᴀʙᴜ ᴠᴄ ᴀᴀ ᴊᴀɪʏᴇ ᴇᴋ ʙᴀʀ 🤨**",
    "**ᴠᴄ ᴘᴀʀ ʏᴇ ʀᴜssɪᴀɴ ᴋʏᴀ ᴋᴀʀ ʀʜɪ ʜᴀɪ 😮‍💨**",
    "**ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ᴠᴀʀɴᴀ ʙᴀɴ ʜᴏ ᴊᴀᴏɢᴇ 🤭**",
    "**sᴏʀʀʏ ʙᴀʙʏ ᴘʟs ᴠᴄ ᴀᴀ ᴊᴀᴏ ɴᴀ 😢**",
    "**ᴠᴄ ᴀᴀɴᴀ ᴇᴋ ᴄʜɪᴊ ᴅɪᴋʜᴀᴛɪ ʜᴜ 😮**",
    "**ᴠᴄ ᴍᴇ ᴄʜᴇᴄᴋ ᴋʀᴋᴇ ʙᴀᴛᴀɴᴀ ᴋᴏɴ sᴀ sᴏɴɢ ᴘʟᴀʏ ʜᴏ ʀʜᴀ ʜᴀɪ.. 💫**",
    "**ᴠᴄ ᴊᴏɪɴ ᴋʀɴᴇ ᴍᴇ ᴋʏᴀ ᴊᴀᴛᴀ ʜᴀɪ ᴛʜᴏʀᴀ ᴅᴇʀ ᴋᴀʀ ʟᴏ ɴᴀ 😇**",
    "**ᴊᴀɴᴇᴍᴀɴ ᴠᴄ ᴀᴀᴏ ɴᴀ ʟɪᴠᴇ sʜᴏᴡ ᴅɪᴋʜᴀᴛɪ ʜᴏᴏɴ.. 😵‍💫**",
    "**ᴏᴡɴᴇʀ ʙᴀʙᴜ ᴠᴄ ᴛᴀᴘᴋᴏ ɴᴀ... 😕**",
    "**ʜᴇʏ ᴄᴜᴛɪᴇ ᴠᴄ ᴀᴀɴᴀ ᴛᴏ ᴇᴋ ʙᴀᴀʀ... 🌟**",
    "**ᴠᴄ ᴘᴀʀ ᴀᴀ ʀʜᴇ ʜᴏ ʏᴀ ɴᴀ... ✨**",
    "**ᴠᴄ ᴘᴀʀ ᴀᴀ ᴊᴀ ᴠʀɴᴀ ɢʜᴀʀ sᴇ ᴜᴛʜᴡᴀ ᴅᴜɴɢɪ... 🌝**",
    "**ʙᴀʙʏ ᴠᴄ ᴘᴀʀ ᴋʙ ᴀᴀ ʀʜᴇ ʜᴏ. 💯**",
    "**ᴍᴇʀɪ ᴊᴀᴀɴ ᴠᴄ ᴀᴀᴋᴇ ᴍᴜᴊʜᴇ ᴅᴇᴋʜ ʟᴏ 🥰**",
    "**ᴄʜᴀʟᴏ ᴠᴄ ᴍᴇ ʙᴇʟᴀᴛᴇ ᴘᴜʀᴀ ʙᴏʀɪɴɢ ʜᴏ ʀʜᴀ 🤐**",
    "**ᴊᴏ ɴᴀ ᴀʏᴇ ᴠᴄ ᴍᴇ ᴜsᴋᴏ ʙʟᴏᴄᴋ 😈**",
    "**ᴠᴄ ᴘᴀʀ ᴀᴀᴏ ɴᴀ ᴍᴇʀɪ ɴɪᴅ ᴄʜᴏʀ ʜᴏ ɢʏɪ 😵**",
    "**ᴄʜᴀʟᴏ ᴠᴄ ᴍᴇ ʀᴏᴍᴀɴᴛɪᴄ ᴍᴏᴏᴅ ʙᴀɴᴀᴛᴇ ʜᴀɪ 😳**",
    "**ᴏʏᴇ ᴠᴄ ᴀᴀ ᴊᴀʟᴅɪ ɴᴀʜɪ ᴛᴏ ᴛʜᴀᴘᴘᴀᴅ 😡**",
    "**ᴠᴄ ᴘʀ ʙᴇʟᴀᴛᴇ ᴍᴏᴠɪᴇ ᴅᴇᴋʜᴛᴇ ʜᴀɪ 🎬**",
    "**ᴠᴄ ᴍᴇ ᴋᴏʏɪ sᴜʀᴘʀɪsᴇ ᴅᴇɴᴀ ʜᴀɪ ᴛᴜᴍʜᴇ 🎁**",
    "**ᴠᴄ ᴘᴀʀ ʜɪ ᴀᴀᴊ ᴋᴀ ᴅᴇᴠɪʟ ᴍᴏᴅᴇ ᴅᴇᴋʜᴇɴɢᴇ 😈**",
    "**ʙᴀʙᴜ ᴠᴄ ᴍᴇ ᴋʜᴀs ʙᴀᴀᴛ ᴋʀɴɪ ʜᴀɪ 💌**",
    "**ᴊᴀʟᴅɪ ᴀᴏ ɴᴀ ᴠᴄ ᴍᴇ, ᴡᴀɪᴛ ɴᴀʜɪ ʜᴏ ʀʜᴀ 😔**",
    "**ᴠᴄ ᴘʀ ᴍᴇʀɪ sɪɴɢɪɴɢ sᴜɴᴏɢᴇ ᴀᴊ 🤭**",
    "**ᴛᴜᴍʜᴀʀᴀ ғᴀᴠᴏᴜʀɪᴛᴇ sᴏɴɢ ʟɢᴀ ʀʜɪ ᴠᴄ ᴍᴇ 🎶**",
    "**ᴠᴄ ᴀᴀᴏ ɴᴀ, ᴇᴋ sᴇᴄʀᴇᴛ ʙᴀᴛᴀᴛɪ ʜᴜ 🤫**",
    "**ᴊᴏɪɴ ᴠᴄ ᴘʀ ᴠᴀʀɴᴀ ᴍᴇ sᴜʟᴋ ʜᴏ ᴊᴀᴜɴɢɪ 😞**",
    "**ᴠᴄ ᴘʀ ᴀᴀᴏ, ᴇᴋ ɴᴇᴡ ᴍᴇᴍᴇ ʙᴀɴᴀɴᴀ ʜᴀɪ 😂**",
    "**ᴠᴄ ᴍᴇ ᴛᴜᴍʜᴀʀɪ ғᴀᴠᴏ ɢᴀʟɪ ᴅᴇᴛɪ ʜᴜ 🤬**",
    "**ᴏʏᴇ ᴠᴄ ᴀᴀ, ᴍᴇʀɪ ʀᴏᴍᴀɴᴛɪᴄ ᴘᴏᴇᴍ sᴜɴᴏ 🌹**",
    "**ᴠᴄ ᴍᴇ ʀᴏᴍᴀɴᴛɪᴄ ᴅᴊ ᴘᴀʀᴛʏ ʜᴏ ʀʜɪ 💃**",
    "**ᴠᴄ ᴀᴀᴏ ɴᴀ, ʙᴀᴄʜᴘᴀɴ ᴋɪ sᴛᴏʀʏ sᴜɴᴀᴛɪ ʜᴜ 🤗**",
    "**ᴊᴏɪɴ ᴠᴄ ғᴀsᴛ, ɢᴏssɪᴘ sᴛᴀʀᴛ ʜᴏ ᴛʜᴀ 😋**",
    "**ᴠᴄ ᴀᴀᴋᴇ sʜᴀʟᴇᴇɴ ʙᴀᴛᴇɴ ᴋʀᴛᴇ ʜᴀɪ 🤭**",
    "**ᴠᴄ ᴀᴀɴᴀ ᴡᴀʀɴᴀ ᴍᴇʀɪ ᴄᴜᴛᴇɴᴇss ᴍɪss ᴋʀᴏɢᴇ 😚**",
    "**ᴠᴄ ᴀᴀ ʀʜᴇ ʜᴏ ʏᴀ ғɪʀ ᴘʀᴏᴘᴏsᴇ ᴋʀᴜ? 💍**",
    "**ᴄʜᴀʟᴏ ᴠᴄ ᴘʀ ᴍᴏᴏᴅ ғʀᴇsʜ ᴋʀᴛᴇ ʜᴀɪ 🌈**",
    "**ᴠᴄ ᴘᴀʀ ᴇᴋ ɴᴇᴡ ᴘʀᴀɴᴋ ᴋʀᴛᴇ ʜᴀɪ 🤪**",
    "**ᴠᴄ ᴀᴀ, ᴍᴇʀɪ ᴅᴜᴘᴀᴛᴛᴀ ᴜᴅᴀ ʀʜᴀ ʜᴀɪ ʙᴀʏᴇʀᴇ 😅**",
    "**ᴠᴄ ᴀᴀᴏ ɴᴀ, ᴇᴋ ᴅɪʟᴄʜᴀsᴘ ɴᴇᴡs ʜᴀɪ 📰**",
    "**ᴠᴄ ᴘʀ ᴄʜᴏᴄᴏʟᴀᴛᴇ ᴅᴇᴛɪ ʜᴜ 🍫**",
    "**ᴠᴄ ᴀᴀᴋᴇ ᴍᴇʀᴇ sᴀᴛʜ ғʟɪʀᴛ ᴋʀᴏ 😏**",
]


@app.on_message(filters.command(["rtag", "tagall"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴅᴏ ᴛʜɪs. ")

    if message.reply_to_message and message.text:
        return await message.reply("⬤ /rtag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("⬤ /rtag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("⬤ /rtag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("⬤ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴅᴏ ᴛʜɪs. ")
    if chat_id in spam_chats:
        return await message.reply("⬤ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["rstop", "tagstop", "vcstop", "tagoff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("⬤ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴅᴏ ᴛʜɪs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♥︎ ᴛᴀɢ sᴛᴏᴘᴘᴇᴅ.")
      

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (suraj08832) 😎

# 🧑‍💻 Developer : t.me/brahix
# 🔗 Source link : GitHub.com/suraj08832/Sonali-MusicV2
# 📢 Telegram channel : t.me/about_brahix
# =======================================================
