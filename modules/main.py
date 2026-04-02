import os, sys, asyncio, requests
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from flask import Flask
from threading import Thread

# Variable Imports
from vars import API_ID, API_HASH, BOT_TOKEN, OWNER, TOTAL_USERS
import globals

# --- KEEP ALIVE SERVER (For Render Free Tier) ---
app = Flask(__name__)
@app.route('/')
def home(): return "Dheeraj Giri Uploader is Online!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
# -----------------------------------------------

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- CLASSY INTERFACE BUTTONS ---
main_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🎙️ Commands", callback_data="all_commands"),
        InlineKeyboardButton("⚙️ Settings", callback_data="setttings")
    ],
    [
        InlineKeyboardButton("💳 Premium", callback_data="upgrade_command"),
        InlineKeyboardButton("📊 Status", callback_data="info_command")
    ],
    [
        InlineKeyboardButton("👤 Contact Owner", url=f"tg://openmessage?user_id={OWNER}")
    ]
])

@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    # Aapka New Classy Welcome Message
    caption = (
        f"👑 **Welcome, {m.from_user.first_name}!**\n\n"
        f"You are now using the official uploader bot of\n"
        f"✨ `𝐃𝐡𝐞𝐞𝐫𝐚𝐣 𝐆𝐢𝐫𝐢`.\n\n"
        f"➠ Submit your TXT file to begin extraction.\n"
        f"➠ High-speed, secure, and 24/7 processing.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"**Official Brand:** `@DheerajGiri_Bots` 🦁"
    )
    
    # Aapka Final DG Logo Direct Link
    logo_wallpaper = "https://i.ibb.co/XQZ1r1n/1000479523.jpg"
    
    await bot.send_photo(
        chat_id=m.chat.id,
        photo=logo_wallpaper, 
        caption=caption,
        reply_markup=main_buttons
    )

# --- REGISTER ALL HANDLERS ---
from text_handler import register_text_handlers
from youtube_handler import register_youtube_handlers
from commands import register_commands_handlers

register_text_handlers(bot)
register_youtube_handlers(bot)
register_commands_handlers(bot)

if __name__ == "__main__":
    keep_alive() 
    print("🚀 Dheeraj Giri Bot is LIVE with Final Branding!")
    bot.run()
