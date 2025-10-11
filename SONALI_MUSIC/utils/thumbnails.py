# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

import os
import re
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
        if draw.textlength(text, font) <= max_width:
            return font
        size -= 1
    return ImageFont.truetype(font_path, min_size)


def get_overlay_content_box(overlay_img: Image.Image):
    alpha = overlay_img.split()[-1]
    threshold = 20
    binary = alpha.point(lambda p: 255 if p > threshold else 0)
    return binary.getbbox()


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

        thumb_path = f"cache/thumb{videoid}.png"
        os.makedirs("cache", exist_ok=True)

        # Download thumbnail
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(thumbnail) as resp:
                    if resp.status == 200:
                        async with aiofiles.open(thumb_path, mode="wb") as f:
                            await f.write(await resp.read())
            youtube = Image.open(thumb_path)
        except:
            async with aiohttp.ClientSession() as session:
                async with session.get(TELEGRAM_AUDIO_URL) as resp:
                    if resp.status == 200:
                        async with aiofiles.open(thumb_path, mode="wb") as f:
                            await f.write(await resp.read())
            youtube = Image.open(thumb_path)

        image1 = changeImageSize(1280, 720, youtube).convert("RGBA")

        # Blur + gradient background
        gradient = Image.new("RGBA", image1.size, (0, 0, 0, 255))
        enhancer = ImageEnhance.Brightness(image1.filter(ImageFilter.GaussianBlur(5)))
        blurred = enhancer.enhance(0.3)
        background = Image.alpha_composite(gradient, blurred)

        draw = ImageDraw.Draw(background)
        font_path = "SONALI_MUSIC/assets/font3.ttf"

        # Player overlay
        player = Image.open("SONALI_MUSIC/assets/sona.png").convert("RGBA").resize((1280, 720))
        overlay_box = get_overlay_content_box(player)
        content_x1, content_y1, content_x2, content_y2 = overlay_box

        # White stroke behind player overlay
        stroke_layer = Image.new("RGBA", background.size, (0, 0, 0, 0))
        stroke = Image.new("RGBA", player.size, (255, 255, 255, 255))
        stroke_layer.paste(stroke, (0, 0), player.split()[-1])
        background = Image.alpha_composite(background, stroke_layer)
        background.paste(player, (0, 0), player)

        # Song thumbnail
        thumb_size = int((content_y2 - content_y1) * 0.55)
        thumb_x = content_x1 + 76
        thumb_y = content_y1 + ((content_y2 - content_y1 - thumb_size) // 2) + 40
        mask = Image.new('L', (thumb_size, thumb_size), 0)
        draw_mask = ImageDraw.Draw(mask)
        radius = int(thumb_size * 0.25)
        draw_mask.rounded_rectangle([(0, 0), (thumb_size, thumb_size)], radius=radius, fill=255)
        thumb_square = youtube.resize((thumb_size, thumb_size))
        thumb_square.putalpha(mask)
        background.paste(thumb_square, (thumb_x, thumb_y), thumb_square)

        # Text positions
        text_x = thumb_x + thumb_size + 30
        title_y = thumb_y + 10
        info_y = title_y + int(thumb_size * 0.33)
        duration_y = info_y + int(thumb_size * 0.28)
        icons_y = duration_y + 40

        # Truncate text
        def truncate_text(text, max_chars=30):
            return (text[:max_chars - 3] + "...") if len(text) > max_chars else text

        short_title = truncate_text(title, max_chars=20)
        short_channel = truncate_text(channel, max_chars=20)

        # Fonts
        title_font = fit_text(draw, short_title, 600, font_path, 42, 28)
        info_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 22)
        duration_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 22)

        # Draw title and channel info
        draw.text((text_x, title_y), f"🎵 {short_title}", (255, 255, 255), font=title_font)
        info_text = f"📺 {short_channel} • {views}"
        draw.text((text_x, info_y), info_text, (200, 200, 200), font=info_font)

        # Duration bar + text
        duration_text = duration if ":" in duration else f"00:{duration.zfill(2)}"
        bar_length = 220
        bar_height = 5
        bar_x = text_x
        bar_y = duration_y
        draw.line([(bar_x, bar_y), (bar_x + bar_length, bar_y)], fill="gray", width=bar_height)
        draw.line([(bar_x, bar_y), (bar_x + bar_length // 3, bar_y)], fill="red", width=bar_height)
        draw.ellipse([(bar_x + bar_length // 3 - 5, bar_y - 5), (bar_x + bar_length // 3 + 5, bar_y + 5)], fill="red")
        draw.text((bar_x, bar_y + 10), "00:00", fill=(200,200,200), font=duration_font)
        draw.text((bar_x + bar_length - 80, bar_y + 10), f"{duration_text}", fill=(200,200,200), font=duration_font)

        # Play icons
        icons_path = "SONALI_MUSIC/assets/play_icons.png"
        if os.path.isfile(icons_path):
            icons_img = Image.open(icons_path).convert("RGBA")
            scale_factor = 0.4
            new_size = (int(icons_img.width*scale_factor), int(icons_img.height*scale_factor))
            icons_img = icons_img.resize(new_size, Image.LANCZOS)
            background.paste(icons_img, (text_x, icons_y), icons_img)

        # Watermark
        watermark_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 24)
        watermark_text = "@Purvi_Bots"
        bbox = draw.textbbox((0,0), watermark_text, font=watermark_font)
        x = background.width - (bbox[2]-bbox[0]) - 25
        y = background.height - (bbox[3]-bbox[1]) - 25
        for dx in (-1,1):
            for dy in (-1,1):
                draw.text((x+dx, y+dy), watermark_text, font=watermark_font, fill=(0,0,0,180))
        draw.text((x,y), watermark_text, font=watermark_font, fill=(255,255,255,240))

        # Cleanup temp thumb
        try: os.remove(f"cache/thumb{videoid}.png")
        except: pass

        tpath = f"cache/{videoid}.png"
        background.save(tpath)
        return tpath

    except Exception as e:
        print(f"[get_thumb Error] {e}")
        traceback.print_exc()
        return None
