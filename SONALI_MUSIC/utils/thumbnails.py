import os
import re
import random
import aiohttp
import aiofiles
import traceback
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch
from config import TELEGRAM_AUDIO_URL

def changeImageSize(maxWidth, maxHeight, image):
    ratio = min(maxWidth / image.size[0], maxHeight / image.size[1])
    newSize = (int(image.size[0] * ratio), int(image.size[1] * ratio))
    return image.resize(newSize, Image.LANCZOS)

def fit_text(draw, text, max_width, font_path, start_size, min_size):
    size = start_size
    while size >= min_size:
        font = ImageFont.truetype(font_path, size)
        if draw.textlength(text, font=font) <= max_width:
            return font
        size -= 1
    return ImageFont.truetype(font_path, min_size)

async def get_thumb(videoid: str):
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        result = (await results.next())["result"][0]

        title = re.sub(r"\W+", " ", result.get("title", "Unsupported Title")).title()
        duration = result.get("duration", "00:00")
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        views = result.get("viewCount", {}).get("short", "Unknown Views")
        channel = result.get("channel", {}).get("name", "Unknown Channel")

        # Live detection
        is_live = not duration or str(duration).strip().lower() in {"", "live", "live now"}
        duration_text = "Live" if is_live else duration or "Unknown"

        thumb_path = f"cache/thumb{videoid}.png"
        os.makedirs("cache", exist_ok=True)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(thumbnail) as resp:
                    if resp.status == 200:
                        async with aiofiles.open(thumb_path, mode="wb") as f:
                            await f.write(await resp.read())
            youtube = Image.open(thumb_path)
        except Exception as e:
            async with aiohttp.ClientSession() as session:
                async with session.get(TELEGRAM_AUDIO_URL) as resp:
                    if resp.status == 200:
                        async with aiofiles.open(thumb_path, mode="wb") as f:
                            await f.write(await resp.read())
            youtube = Image.open(thumb_path)

        image1 = changeImageSize(1280, 720, youtube).convert("RGBA")

        gradient = Image.new("RGBA", image1.size, (0, 0, 0, 255))
        enhancer = ImageEnhance.Brightness(image1.filter(ImageFilter.GaussianBlur(5)))
        blurred = enhancer.enhance(0.3)
        background = Image.alpha_composite(gradient, blurred)

        draw = ImageDraw.Draw(background)
        font_path = "SONALI_MUSIC/assets/font3.ttf"

        player = Image.open("SONALI_MUSIC/assets/sona.png").convert("RGBA").resize((1280, 720))
        background.paste(player, (0, 0), player)

        # --- Thumbnail box ---
        thumb_size = 340
        thumb_x, thumb_y = 120, 240
        mask = Image.new('L', (thumb_size, thumb_size), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (thumb_size, thumb_size)], radius=80, fill=255)
        thumb_square = youtube.resize((thumb_size, thumb_size))
        thumb_square.putalpha(mask)
        background.paste(thumb_square, (thumb_x, thumb_y), thumb_square)

        # --- Text positions ---
        text_x = thumb_x + thumb_size + 60
        title_y = thumb_y + 20
        info_y = title_y + 100

        # --- Title & Channel Info ---
        title_font = fit_text(draw, title, 600, font_path, 42, 28)
        draw.text((text_x, title_y), title, (255, 255, 255), font=title_font)

        info_text = f"{channel} • {views}"
        info_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 26)
        draw.text((text_x, info_y), info_text, (200, 200, 200), font=info_font)

        # --- Progress Bar ---
        bar_x, bar_y = text_x, info_y + 50
        bar_total_len = 480
        bar_red_len = 180
        draw.line([(bar_x, bar_y), (bar_x + bar_total_len, bar_y)], fill="gray", width=6)
        draw.line([(bar_x, bar_y), (bar_x + bar_red_len, bar_y)], fill="red", width=6)
        draw.ellipse([(bar_x + bar_red_len - 8, bar_y - 8),
                      (bar_x + bar_red_len + 8, bar_y + 8)], fill="red")

        # --- Duration Text ---
        time_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 24)
        draw.text((bar_x, bar_y + 12), "00:00", fill="white", font=time_font)
        draw.text(
            (bar_x + bar_total_len - (70 if is_live else 60), bar_y + 12),
            duration_text,
            fill="red" if is_live else "white",
            font=time_font
        )

        # --- Play Icons ---
        icons_path = "SONALI_MUSIC/assets/play_icons.png"
        if os.path.isfile(icons_path):
            ICONS_W, ICONS_H = 320, 40
            ICONS_X = text_x + 70
            ICONS_Y = bar_y + 60
            ic = Image.open(icons_path).resize((ICONS_W, ICONS_H)).convert("RGBA")
            r, g, b, a = ic.split()
            white_ic = Image.merge("RGBA", (r.point(lambda *_: 255), g.point(lambda *_: 255), b.point(lambda *_: 255), a))
            background.paste(white_ic, (ICONS_X, ICONS_Y), white_ic)

        # --- Watermark ---
        watermark_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 22)
        watermark_text = "@Purvi_Bots"
        x = background.width - 200
        y = background.height - 40
        draw.text((x, y), watermark_text, font=watermark_font, fill=(255, 255, 255, 240))

        try:
            os.remove(thumb_path)
        except:
            pass

        tpath = f"cache/{videoid}.png"
        background.save(tpath)
        return tpath

    except Exception as e:
        print(f"[get_thumb Error] {e}")
        traceback.print_exc()
        return None
