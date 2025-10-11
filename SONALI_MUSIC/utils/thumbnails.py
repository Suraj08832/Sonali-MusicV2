import os
import re
import random
import aiohttp
import aiofiles
import traceback

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
from config import TELEGRAM_AUDIO_URL


def changeImageSize(maxWidth, maxHeight, image):
    ratio = min(maxWidth / image.size[0], maxHeight / image.size[1])
    newSize = (int(image.size[0] * ratio), int(image.size[1] * ratio))
    return image.resize(newSize, Image.LANCZOS)  


def truncate(text, max_chars=50):
    words = text.split()
    text1, text2 = "", ""
    for word in words:
        if len(text1 + " " + word) <= max_chars and not text2:
            text1 += " " + word
        else:
            text2 += " " + word
    return [text1.strip(), text2.strip()]


def fit_text(draw, text, max_width, font_path, start_size, min_size):
    try:
        size = start_size
        while size >= min_size:
            font = ImageFont.truetype(font_path, size)
            if draw.textlength(text, font=font) <= max_width:
                return font
            size -= 1
        return ImageFont.truetype(font_path, min_size)
    except:
        # Fallback font agar font3.ttf nahi mila toh
        try:
            return ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", start_size)
        except:
            return ImageFont.load_default()


def get_overlay_content_box(overlay_img: Image.Image) -> tuple:
    """Returns bounding box (x1, y1, x2, y2) of the semi-transparent content box in overlay."""
    alpha = overlay_img.split()[-1]  # Extract alpha channel
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

        print(f"[DEBUG] Title: {title}")  # Debug line
        print(f"[DEBUG] Channel: {channel}")  # Debug line
        print(f"[DEBUG] Views: {views}")  # Debug line

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
        except Exception as e:
            print(f"[Thumbnail Download Failed] Using default image. Error: {e}")
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
        
        # Font paths with fallback
        font_path = "SONALI_MUSIC/assets/font3.ttf"
        if not os.path.exists(font_path):
            font_path = "SONALI_MUSIC/assets/font.ttf"  # Fallback to font.ttf

        # Player overlay
        player = Image.open("SONALI_MUSIC/assets/sona.png").convert("RGBA").resize((1280, 720))
        
        # Add white stroke - FIXED THIS PART
        stroke_layer = Image.new("RGBA", (1280, 720), (255, 255, 255, 0))
        stroke_draw = ImageDraw.Draw(stroke_layer)
        # Add stroke effect around player
        for dx, dy in [(-2,-2), (-2,2), (2,-2), (2,2)]:
            stroke_layer.paste(player, (dx, dy), player)
        
        background = Image.alpha_composite(background, stroke_layer)
        background.paste(player, (0, 0), player)

        overlay_box = get_overlay_content_box(player) 
        if overlay_box:
            content_x1, content_y1, content_x2, content_y2 = overlay_box
        else:
            # Default coordinates agar overlay_box None hai
            content_x1, content_y1, content_x2, content_y2 = 100, 100, 1180, 620

        # Song thumbnail (square)
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

        # Text positions - IMPROVED POSITIONING
        text_x = thumb_x + thumb_size + 30
        title_y = thumb_y + 5
        info_y = title_y + 45  # Fixed gap
        duration_y = info_y + 35  # Fixed gap
        icons_y = duration_y + 35  # Fixed gap

        def truncate_text(text, max_chars=25):
            return (text[:max_chars - 3] + "...") if len(text) > max_chars else text

        short_title = truncate_text(title, max_chars=25)
        short_channel = truncate_text(channel, max_chars=25)

        # Fonts - WITH ERROR HANDLING
        try:
            title_font = fit_text(draw, short_title, 600, font_path, 42, 28)
            info_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 22)
            duration_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 20)
        except Exception as font_error:
            print(f"[FONT ERROR] Using default fonts: {font_error}")
            title_font = ImageFont.load_default()
            info_font = ImageFont.load_default()
            duration_font = ImageFont.load_default()

        # Draw title and channel info - WITH EMOJIS
        draw.text((text_x, title_y), f"{short_title}", (255, 255, 255), font=title_font)
        info_text = f"{short_channel} • {views}"
        draw.text((text_x, info_y), info_text, (200, 200, 200), font=info_font)

        # Duration bar + text
        duration_text = duration if ":" in duration else f"00:{duration.zfill(2)}"
        
        # Progress bar
        bar_length = 220
        bar_height = 5
        bar_x = text_x
        bar_y = duration_y
        
        # Progress bar background
        draw.rounded_rectangle([(bar_x, bar_y), (bar_x + bar_length, bar_y + bar_height)], 
                             radius=3, fill=(100, 100, 100))
        
        # Progress bar fill (25% progress)
        progress_width = int(bar_length * 0.25)
        draw.rounded_rectangle([(bar_x, bar_y), (bar_x + progress_width, bar_y + bar_height)], 
                             radius=3, fill=(255, 0, 0))
        
        # Progress knob
        knob_x = bar_x + progress_width
        draw.ellipse([(knob_x - 4, bar_y - 4), (knob_x + 4, bar_y + bar_height + 4)], 
                    fill=(255, 255, 255))
        
        # Duration text
        draw.text((bar_x, bar_y + 12), "00:00", fill=(200, 200, 200), font=duration_font)
        draw.text((bar_x + bar_length - 60, bar_y + 12), f"{duration_text}", 
                 fill=(200, 200, 200), font=duration_font)

        # Play icons
        icons_path = "SONALI_MUSIC/assets/play_icons.png"
        if os.path.isfile(icons_path):
            try:
                icons_img = Image.open(icons_path).convert("RGBA")
                icons_w, icons_h = icons_img.size
                scale_factor = 0.35
                new_size = (int(icons_w * scale_factor), int(icons_h * scale_factor))
                icons_img = icons_img.resize(new_size, Image.LANCZOS)
                icons_x = text_x
                background.paste(icons_img, (icons_x, icons_y), icons_img)
            except Exception as icon_error:
                print(f"[ICON ERROR] {icon_error}")

        # Watermark
        try:
            watermark_font = ImageFont.truetype("SONALI_MUSIC/assets/font.ttf", 24)
            watermark_text = "@Purvi_Bots"
            
            if hasattr(draw, "textbbox"): 
                bbox = draw.textbbox((0, 0), watermark_text, font=watermark_font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
            else:  
                text_width, text_height = draw.textsize(watermark_text, font=watermark_font)

            x = background.width - text_width - 25
            y = background.height - text_height - 25
            
            # Text shadow
            for dx in (-1, 1):
                for dy in (-1, 1):
                    draw.text((x + dx, y + dy), watermark_text, font=watermark_font, fill=(0, 0, 0, 180))
            draw.text((x, y), watermark_text, font=watermark_font, fill=(255, 255, 255, 240))
        except:
            pass

        # Cleanup temp thumb
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass

        tpath = f"cache/{videoid}.png"
        background.save(tpath)
        print(f"[SUCCESS] Thumbnail saved: {tpath}")  # Debug line
        return tpath

    except Exception as e:
        print(f"[get_thumb Error] {e}")
        traceback.print_exc()
        return None
