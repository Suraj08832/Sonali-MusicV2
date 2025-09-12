# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
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

TAGMES = [ " **※ ɪ ʟᴏᴠᴇ ʏᴏᴜ...ᰔᩚ**",
           " **※ ғᴏʀɢᴇᴛ ᴍᴇ..ᰔᩚ",
           " **※ ɪ ᴅᴏɴ'ᴛ ʟᴏᴠᴇ ʏᴏᴜ...ᰔᩚ**",
           " **※ ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀs ᴘɪʏᴀ, ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀs...ᰔᩚ**",
           " **※ ᴊᴏɪɴ ᴍʏ ɢʀᴏᴜᴘ ᴀʟsᴏ...ᰔᩚ**",
           " **※ ɪ ᴋᴇᴘᴛ ʏᴏᴜʀ ɴᴀᴍᴇ ɪɴ ᴍʏ ʜᴇᴀʀᴛ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴀʀᴇ ᴀʟʟ ʏᴏᴜʀ ғʀɪᴇɴᴅs...ᰔᩚ**",
           " **※ ɪɴ ᴡʜᴏsᴇ ᴍᴇᴍᴏʀʏ ᴀʀᴇ ʏᴏᴜ ʟᴏsᴛ ᴍʏ ʟᴏᴠᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛs ʏᴏᴜʀ ᴘʀᴏғᴇssɪᴏɴ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴅɪᴅ ʏᴏᴜ ʟɪᴠᴇ...ᰔᩚ**",
           " **※ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʙᴀʙʏ...ᰔᩚ**",
           " **※ ɢᴏᴏᴅ ɴɪɢʜᴛ, ɪᴛ's ᴠᴇʀʏ ʟᴀᴛᴇ...ᰔᩚ**",
           " **※ ɪ ғᴇᴇʟ ᴠᴇʀʏ sᴀᴅ ᴛᴏᴅᴀʏ...ᰔᩚ**",
           " **※ ᴛᴀʟᴋ ᴛᴏ ᴍᴇ ᴛᴏᴏ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ's ғᴏʀ ᴅɪɴɴᴇʀ ᴛᴏᴅᴀʏ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ's ɢᴏɪɴɢ ᴏɴ...ᰔᩚ**",
           " **※ ᴡʜʏ ᴅᴏɴ'ᴛ ʏᴏᴜ ᴍᴇssᴀɢᴇ...ᰔᩚ**",
           " **※ ɪ ᴀᴍ ɪɴɴᴏᴄᴇɴᴛ...ᰔᩚ**",
           " **※ ɪᴛ ᴡᴀs ғᴜɴ ʏᴇsᴛᴇʀᴅᴀʏ, ᴡᴀsɴ'ᴛ ɪᴛ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴡᴇʀᴇ ʏᴏᴜ ʙᴜsʏ ʏᴇsᴛᴇʀᴅᴀʏ...ᰔᩚ**",
           " **※ ʏᴏᴜ ʀᴇᴍᴀɪɴ sᴏ ᴄᴀʟᴍ ғʀɪᴇɴᴅ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sɪɴɢ, sɪɴɢ...ᰔᩚ**",
           " **※ ᴡɪʟʟ ʏᴏᴜ ᴄᴏᴍᴇ ғᴏʀ ᴀ ᴡᴀʟᴋ ᴡɪᴛʜ ᴍᴇ...ᰔᩚ**",
           " **※ ᴀʟᴡᴀʏs ʙᴇ ʜᴀᴘᴘʏ ғʀɪᴇɴᴅ...ᰔᩚ**",
           " **※ ᴄᴀɴ ᴡᴇ ʙᴇ ғʀɪᴇɴᴅs...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ᴍᴀʀʀɪᴇᴅ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ʜᴀᴠᴇ ʏᴏᴜ ʙᴇᴇɴ ʙᴜsʏ ғᴏʀ sᴏ ᴍᴀɴʏ ᴅᴀʏs...ᰔᩚ**",
           " **※ ʟɪɴᴋ ɪs ɪɴ ʙɪᴏ, ᴛᴏ ᴊᴏɪɴ ɴᴏᴡ...ᰔᩚ**",
           " **※ ʜᴀᴅ ғᴜɴ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴇᴠᴇʀ ʀᴇᴍᴇᴍʙᴇʀ ᴍᴇ...ᰔᩚ**",
           " **※ ʟᴇᴛ's ᴘᴀʀᴛʏ...ᰔᩚ**",
           " **※ ʜᴏᴡ ᴄᴏᴍᴇ ᴛᴏᴅᴀʏ...ᰔᩚ**",
           " **※ ʟɪsᴛᴇɴ ᴍᴇ...ᰔᩚ**",
           " **※ ʜᴏᴡ ᴡᴀs ʏᴏᴜʀ ᴅᴀʏ...ᰔᩚ**",
           " **※ ᴅɪᴅ ʏᴏᴜ sᴇᴇ...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ᴛʜᴇ ᴀᴅᴍɪɴ ʜᴇʀᴇ...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ɪɴ ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ...ᰔᩚ**",
           " **※ ᴀɴᴅ ʜᴏᴡ ɪs ᴛʜᴇ ᴘʀɪsᴏɴᴇʀ...ᰔᩚ**",
           " **※ sᴀᴡ ʏᴏᴜ ʏᴇsᴛᴇʀᴅᴀʏ...ᰔᩚ**",
           " **※ ᴡʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜ ғʀᴏᴍ...ᰔᩚ**",
           " **※ ᴀʀᴇ ʏᴏᴜ ᴏɴʟɪɴᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ᴇᴀᴛ...ᰔᩚ**",
           " **※ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ɪ ᴡɪʟʟ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴀɴᴅ ᴛᴀɢ ᴇᴠᴇʀʏᴏɴᴇ...ᰔᩚ**",
           " **※ ᴡɪʟʟ ʏᴏᴜ ᴘʟᴀʏ ᴛʀᴜᴛʜ ᴀɴᴅ ᴅᴀʀᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛs ʜᴀᴘᴘᴇɴᴇᴅ ᴛᴏ ʏᴏᴜ...ᰔᩚ**",
           " **※ ᴅᴏ ʏᴏᴜ ᴡᴀɴɴᴀ ᴇᴀᴛ ᴄʜᴏᴄᴏʟᴀᴛᴇ...ᰔᩚ**",
           " **※ ʜᴇʟʟᴏ ʙᴀʙʏ...ᰔᩚ**",
           " **※ ᴅᴏ ᴄʜᴀᴛᴛɪɴɢ ᴡɪᴛʜ ᴍᴇ...ᰔᩚ**",
           " **※ ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ sᴀʏ...ᰔᩚ**",
           " **※ ɢɪᴠᴇ ᴍᴇ ʏᴏᴜʀ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ ᴘʟᴇᴀsᴇ...ᰔᩚ**"
           ]

VC_TAG = [
    " **हमके भुला जइबू...💥**",
    " **हम तोहरा से मोहब्बत नइखीं करत...💥**",
    " **एकरा के आपन बना ल, पिया...💥**",
    " **हमरा ग्रुप में जॉइन कर ल @Oye_Careless ...💥**",
    " **तोहार नाम दिल में लिखनी ह...💥**",
    " **तोहार सगरी संगी कहां बा लोग...💥**",
    " **केहू के याद में खो गइल बाड़ू का...💥**",
    " **तोहार काम कवन ह...💥**",
    " **कहां रहेलू तू...💥**",
    " **शुभ प्रभात, बाबू...💥**",
    " **शुभ रात्री, बहुत देर हो गइल...💥**",
    " **आज हमार मन बड़ा खराब बा...💥**",
    " **हमसे भी बतिया ल...💥**",
    " **आज रात के खाए में का बनल बा...💥**",
    " **का हो रहल बा...💥**",
    " **तू मैसेज काहे नइख देत...💥**",
    " **हम शरीफ बानी नु...💥**",
    " **काल मजा आइल ना...💥**",
    " **तू काल कहां बिजी रहले...💥**",
    " **तू कवनो रिलेशन में बाड़ू का...💥**",
    " **तू बहुत शांत रहेलू, दोस्त...💥**",
    " **तू गाना गा सकताड़ू का...💥**",
    " **हमरा संग घूमे चलबू का...💥**",
    " **सदा मुस्कुरा के रहs, दोस्त...💥**",
    " **हमनी के दोस्त बन सकीला का...💥**",
    " **तू बियाहल बाड़ू का...💥**",
    " **एतना दिन कहां गायब रहले...💥**",
    " **लिंक बायो में बा, अब जॉइन कर...💥**",
    " **मजाक कइनी...💥**",
    " **तू ग्रुप के मालिक के जानताड़ू का...💥**",
    " **तू कबो हमके याद करेलू का...💥**",
    " **चल पार्टी करीलें...💥**",
    " **आज के दिन कइसन गइल...💥**",
    " **तोहार दिन कइसन गइल...💥**",
    " **तू देखले बा का...💥**",
    " **तू ए ग्रुप के एडमिन बाड़ू का...💥**",
    " **हमनी के दोस्त बन सकीला...💥**",
    " **तू रिलेशनशिप में बाड़ू का...💥**",
    " **और सब कइसन बा...💥**",
    " **काल हम तोहके देखनी...💥**",
    " **तू कहां के बाड़ू...💥**",
    " **तू ऑनलाइन बाड़ू का...💥**",
    " **तू हमार दोस्त बाड़ू का....💥**",
    " **तू का खाए के पसंद करेलू...💥**",
    " **हमके आपन ग्रुप में ऐड करा, हम गाना बजाइब आ सबके टेग करब....💥**",
    " **आज हम दुखी बानी...💥**",
    " **तू ट्रुथ एंड डेयर खेलबू का...💥**",
    " **तोहार जइसन दोस्त होखला से का डर...💥**",
    " **का भइल तोहके...💥**",
    " **तू चॉकलेट खइबू का....💥**",
    " **हेलो बाबू...💥**",
    " **हमसे बात करs...💥**",
    " **तू का कहताड़ू...💥**",
    " **सोनाली के ह...💥**"
    " **का रे, फोन खा गइल बा का... जवाब नइखे आवत...💥**",
    " **हम त अब बात भी ना करबs तोसे... बहुत हो गइल नाटक...💥**",
    " **तू त निकले बड़का धोखेबाज...💥**",
    " **हमके त लगल तू सुधर गइल बाड़ू... लेकिन ना...💥**",
    " **तोहार attitude देख के त कुत्ता भी शरमा जाई...💥**",
    " **तू बा त बड़ा खास... बाकिर दिमाग कम बाड़ू...💥**",
    " **अरे बाबू, एतना टशन में मत रहा, नेट कट हो जाई...💥**",
    " **तू रहs हमसे दूर, नाहीं त दिल चुरइबs...💥**",
    " **तू हमके भाव देबे ना, ठीक बा, Netflix देखब...💥**",
    " **बोलs ना रे बकखिलवा... चुप काहे बाड़ू...💥**",
    " **एतना attitude ठीक नइखे, हमरा से बात करs...💥**",
    " **हमरा सामने hero बनबू त ego तोड़ देब...💥**",
    " **अरे बाबू, तू बाड़ू कि बिजली... हरदम झटका देताड़ू...💥**",
    " **हमसे पंगा नइ लेबे के चाहीं, हमरा पास टेगिंग पावर बा...💥**",
    " **तू त बढ़िया झूठ बोल लेताड़ू... शादी में भी speech दे सकs...💥**",
    " **बात करs ना, नाहीं त हम group में tag कर-कर के परेशान करब...💥**",
    " **तू जवाब ना देबू त हम गाना छोड़ के ताना मारब...💥**",
    " **हमसे बात करs, नाहीं त VC में रोअत आवाज भेजब...💥**",
    " **तू ignore करबू त हम reels बना-बना के viral करब...💥**",
    " **हमार दिल त टूट गइल... अब status तोहपे लिखब...💥**",
    " **जा ना, हम तोहके block कर देब... 5 मिनट बाद unblock भी करब...💥**",
    " **तोहार attitude त IPL से भी जादा over-rated बा...💥**",
    " **हमार भी ego बा, बाकिर हम तोहसे बात करे चल आइल...💥**",
    " **तू reply देबू ना त हम VC में तेरा नाम चिल्लाईब...💥**",
    " **Tag mat करs, हम busy बानी... मतलब online लेकिन movie में बानी...💥**",
    " **बोलs ना, नाहीं त हम तोहके ‘seen’ से मारब...💥**",
    " **तू त हर बात पे seen कर देताड़ू, दिल ना तड़पे तो का खून बहे?...💥**",
    " **हमरो ego बा, बाकिर तोहार online देख के melt हो जाला...💥**",
    " **तू reply ना दे, हम status पर तोहार नाम लिखब...💥**",
    " **ए बाबू, बात करs नाहीं त group के admin बदल देब...💥**",
    " **जबसे तू busy कहके gayab भइल, तबसे wifi से नफरत हो गइल...💥**",
    " **तोहार बात याद आइल त mobile से भी जलन होखे लागल...💥**",
    " **तू दिल तोड़s, हम meme बना के viral कर देब...💥**",
    " **तू हमरा से बात नइख करत, लेकिन देख लिह, tag त मिलत रहल...💥**",
    " **तू smile करताड़ू, बाकिर हम tag से तोहार नींद उड़ाईब...💥**",
    " **तू block करबू त हम screenshot लगा के कहानी बना देब...💥**",
    " **तू ignore करs, हम tag में तोहरा नाम के महाभारत लिखब...💥**",
    " **हमसे बात करs वरना VC में बवाल मच जाई...💥**",
    " **तू त निकले chat का खिलाड़ी, सबके seen पर out कर देताड़ू...💥**",
    " **तोहार याद त हर tag में समाइल बा, बस तू बा कि गायब बाड़ू...💥**",
    " **तोहार जवाब त चांद जइसन हो गइल बा, बहुत देर में दिखाई देला...💥**",
    " **तू बात नइख करत, हम tag में break-up announcement कर देब...💥**",
    " **हमरा से बात ना करबू त group में रोवत emoji spam हो जाई...💥**",
    " **एतना attitude त राजा भोज के भी ना रहल...💥**",
    " **हमके ignore करके तू का पाईबs, guilt के gold medal?...💥**",
    " **तू चुप रहलs, हम loudspeaker लेके VC में आ जाईब...💥**",
    " **Group में एतना चुप मत रहा, कहीं internet फेल त ना हो गइल?...💥**",
    " **बात करs, नाहीं त हम तोहरा नाम पर VC बना देब...💥**",
    " **तू हमार crush रहू, अब tag list में permanent guest बाड़ू...💥**",
    " **चल झूठा, busy त हम भी बानी, लेकिन text कर देनी...💥**",
    " **तू बात करs, नाहीं त हम Google पे सर्च करब 'missing friend remedy'...💥**",
          
]


@app.on_message(filters.command(["entag", "englishtag" ], prefixes=["/", "@", "#"]))
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
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("⬤ /entag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("⬤ /entag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("⬤ /entag ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
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


@app.on_message(filters.command(["bhtag"], prefixes=["/", "@", "#"]))
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
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
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



@app.on_message(filters.command(["enstop", "bhstop"]))
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
        return await message.reply("⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♥︎ ᴛᴀɢ sᴛᴏᴘᴘᴇᴅ.")

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
