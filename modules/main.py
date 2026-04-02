import os, sys, asyncio, requests
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, InputMediaPhoto
from flask import Flask
from threading import Thread

# Variable Imports
from vars import API_ID, API_HASH, BOT_TOKEN, OWNER, CREDIT, AUTH_USERS, TOTAL_USERS
import globals

# Handler Imports (Same as before)
from html_handler import register_html_handlers
from drm_handler import register_drm_handlers
from text_handler import register_text_handlers
from features import register_feature_handlers
from upgrade import register_upgrade_handlers
from commands import register_commands_handlers
from settings import register_settings_handlers
from broadcast import register_broadcast_handlers
from youtube_handler import register_youtube_handlers
from authorisation import register_authorisation_handlers

# --- FLASK SERVER (For Render Free Tier) ---
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
# -------------------------------------------

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    # Branding change kar di hai
    caption = (
        f"𝐇𝐞𝐥𝐥𝐨 **{m.from_user.first_name}** 👋!\n\n"
        f"➠ 𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐁𝐨𝐭\n"
        f"➠ 𝐌𝐚𝐝𝐞 𝐁𝐲 : [𝐃𝐡𝐞𝐞𝐫𝐚𝐣 𝐁𝐨𝐭𝐬](tg://openmessage?user_id={OWNER}) 🦁"
    )
    await bot.send_photo(
        chat_id=m.chat.id,
        photo="https://iili.io/KuCBoV2.jpg",
        caption=caption,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎙️ Commands", callback_data="cmd_command")]])
    )

# Register All Handlers
register_text_handlers(bot)
register_html_handlers(bot)
register_feature_handlers(bot)
register_settings_handlers(bot)
register_upgrade_handlers(bot)
register_commands_handlers(bot)
register_broadcast_handlers(bot)
register_youtube_handlers(bot)
register_authorisation_handlers(bot)
register_drm_handlers(bot)

if __name__ == "__main__":
    keep_alive() # Flask start karo
    print("Bot is starting on Web Service...")
    bot.run()
